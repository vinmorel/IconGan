import os
import requests 
import zipfile 
import shutil
from os import listdir
from os.path import isfile, join

def DownloadUrl(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def UnZipFolder(zipFilePath, datasetPath):
    savePath = datasetPath + "temp/"

    with zipfile.ZipFile(zipFilePath, 'r') as zip:
        files_in_zip = zip.namelist()
        sourceFolderPath = savePath + files_in_zip[3]

        for fname in files_in_zip[4:]:
            zip.extract(fname, savePath)
    
    MoveFiles(sourceFolderPath, datasetPath, savePath)
        
def MoveFiles(sourceFolder, datasetPath, tempPath):
    onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
    for fpath in onlyfiles:
        shutil.move(sourceFolder + fpath, datasetPath + fpath.split(".")[0] + ".png")
    shutil.rmtree(tempPath)


def MakeDataset(url, datasetPath):
    zipFolderPath = datasetPath + "temp.zip"
    DownloadUrl(url, zipFolderPath)
    UnZipFolder(zipFolderPath, datasetPath)
    os.remove(zipFolderPath)

if __name__ == "__main__":
    datasetPath = "C:/Users/vin_m/Desktop/Git/IconGan/Dataset/"
    url = "https://iconarchive.com/download/s520/icehouse/smurf/smurfs.zip"

    MakeDataset(url, datasetPath)