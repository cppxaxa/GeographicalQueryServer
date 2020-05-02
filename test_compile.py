import json
import os
from lib.Compiler import *

class CompilerFactory:
    @staticmethod
    def defaultCompiler(lowendHardware):
        compiler = Compiler(lowendHardware)

        osmParserQueries = None
        with open("lib\\OsmParserQueries.json") as f:
            osmParserQueries = json.load(f)

        paramIPairs = osmParserQueries["Osmparser"]["parameter_i"]
        for k in paramIPairs:
            osmParserCompiler = OsmParserCompiler("java", "bin\\osmparser\\osmparser-0.13.jar", paramIPairs[k], k)
            compiler.addCompiler(osmParserCompiler)
        
        # Seabeach and coastline
        outputId = "AllCoast"
        paramI = paramIPairs["Seabeach"] + " " + paramIPairs["Coastline"]
        osmParserCompiler = OsmParserCompiler("java", "bin\\osmparser\\osmparser-0.13.jar", paramI, outputId)
        compiler.addCompiler(osmParserCompiler)

        # River and riverbank
        outputId = "AllRiver"
        paramI = paramIPairs["River"] + " " + paramIPairs["Riverbank"]
        osmParserCompiler = OsmParserCompiler("java", "bin\\osmparser\\osmparser-0.13.jar", paramI, outputId)
        compiler.addCompiler(osmParserCompiler)

        return compiler

def compile():
    swConfig = None
    with open("Configuration.json") as f:
        swConfig = json.load(f)

    rawOsmV1Dir = swConfig["RawOsmV1"]["path"]
    compiledGeographyDir = swConfig["CompiledGeography"]["path"]
    compiledGeographyCurrentVersionFile = os.path.join( \
        compiledGeographyDir, swConfig["CompiledGeography"]["versionFilename"])
    lowendHardware = swConfig["Compilation"]["lowendHardware"]

    # Write the configuration
    version = 1
    if os.path.exists(compiledGeographyCurrentVersionFile):
        with open(compiledGeographyCurrentVersionFile) as f:
            ver = int(f.readline())
            version = ver + 1
    with open(compiledGeographyCurrentVersionFile, "w") as f:
        f.write(str(version))

    # Trigger the compilation
    compiler = CompilerFactory.defaultCompiler(lowendHardware)
    compiler.compile(rawOsmV1Dir, compiledGeographyDir)


if __name__ == "__main__":
    compile()