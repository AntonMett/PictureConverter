from pathlib import Path
from PIL import Image
import sys

inputPath = Path(sys.argv[1])
inputFiles = inputPath.glob("**/*.jpg")
outputPath = Path(f'{inputPath}\{sys.argv[2]}')
outputPath.mkdir()
for f in inputFiles:
    outputFile = outputPath / Path(f.stem + ".png")
    im = Image.open(f)
    im.save(outputFile)
