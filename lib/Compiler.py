import time
import subprocess
import json
import os

class Compiler:
    def __init__(self, lowendHardware, maxProc):
        self.sequence = []
        self.lowendHardware = lowendHardware
        self.maxProc = maxProc

    def addCompiler(self, compiler):
        self.sequence.append(compiler)

    def addWaitAll(self):
        self.sequence.append(WaitAllCompiler())

    def compile(self, inputDir, outputDir):
        startTime = time.perf_counter()
        total = len(self.sequence)
        curr = 0

        processes = []

        for el in self.sequence:
            curr += 1

            if len(processes) >= self.maxProc:
                for proc in processes:
                    proc.wait()
                processes = []

            print("Step {}/{}".format(curr, total))

            if el is not WaitAllCompiler:
                proc = el.compile(inputDir, outputDir, self.lowendHardware)

                processes.append(proc)
            else:
                for proc in processes:
                    proc.wait()
                processes = []
        
        if self.sequence[-1] is not WaitAllCompiler:
            for proc in processes:
                proc.wait()
        
        endTime = time.perf_counter()
        print("Finished compilation, Elapsed time: {} seconds".format(str(endTime - startTime)))


class PlaceToFileMappingCompiler:
  def __init__(self, compiledGeographyMetadataFilename):
    self.compiledGeographyMetadataFilename = compiledGeographyMetadataFilename

  def compile(self, inputDir, outputDir, lowendHardware):
    completeGeographyOutputFilename = os.path.join(outputDir, self.compiledGeographyMetadataFilename)

    mapping = {
        "Types": ["Coast", "River", "OnlyCoastline", "HighwayPrimary", "OnlyRiver", \
            "OnlyRiverbank", "Road", "OnlySeabeach", "Waterbody", "Waterway", "RoadCurve"], 
        "Mapping": {
            "Coast": "AllCoast.json",
            "River": "AllRiver.json",
            "OnlyCoastline": "Coastline.json",
            "HighwayPrimary": "HighwayPrimary.json",
            "OnlyRiver": "River.json",
            "OnlyRiverbank": "Riverbank.json",
            "Road": "Road,json",
            "OnlySeabeach": "Seabeach.json",
            "Waterbody": "WaterBody.json",
            "Waterway": "Waterway.json",
            "RoadCurve": "RoadCurve.json"
        }
    }

    with open(completeGeographyOutputFilename, 'w') as f:
      f.write(json.dumps(mapping))
    
    return WaitingObject()


class OsmParserCompiler:
    def __init__(self, javaExec, osmparserJarPath, parameterI, outputId):
        self.javaExec = javaExec
        self.osmparserJarPath = osmparserJarPath
        self.parameterI = parameterI
        self.outputId = outputId
    
    def constructCmd(self, inputFile, outputFile):
        return self.javaExec + " -jar " + self.osmparserJarPath \
            + " -f " + inputFile + " -o " + outputFile \
                + " -i " + self.parameterI

    def compile(self, inputDir, outputDir, lowendHardware):
        files = []
        for filename in os.listdir(inputDir):
            if os.path.splitext(filename)[1].strip().lower() != ".osm":
                continue

            completeInputFilename = os.path.join(inputDir, filename)
            files.append(completeInputFilename)

        completeOutputFilename = os.path.join(outputDir, self.outputId + ".json")
        command = self.constructCmd(" ".join(files), completeOutputFilename)

        print("   " + command)

        process = subprocess.Popen(command, shell=True)

        if lowendHardware:
            process.wait()

        return process
        

class WaitingObject:
    def __init__(self, process = None):
        self.process = process

    def wait(self):
        if self.process is not None:
            self.process.wait()

class WaitAllCompiler:
    def compile(self, inputDir, outputDir, lowendHardware):
        return WaitingObject()


