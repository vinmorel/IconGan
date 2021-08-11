from os import listdir
from os.path import isfile, join
from PIL import Image, ImageDraw


datasetPath = "C:/Users/vin_m/Desktop/Git/IconGan/Dataset/"
onlyfiles = [join(datasetPath, f) for f in listdir(datasetPath) if isfile(join(datasetPath, f))]

for fname in onlyfiles:
    img = Image.open(fname)

    h, w = img.size
    if (h != 32 or w != 32):
        print(fname)