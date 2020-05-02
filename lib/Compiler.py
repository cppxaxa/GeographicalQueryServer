
import subprocess
import json
import os

class Compiler:
    def __init__(self, lowendHardware):
        self.sequence = []
        self.lowendHardware = lowendHardware

    def addCompiler(self, compiler):
        self.sequence.append(compiler)

    def compile(self, inputDir, outputDir):
        total = len(self.sequence)
        curr = 0
        for el in self.sequence:
            curr += 1
            print("Step {}/{}".format(curr, total))
            el.compile(inputDir, outputDir, self.lowendHardware)

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
        process.wait()
        



