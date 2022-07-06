import os
import math
import shutil
import main


for file in os.scandir("output/faces"):
    if not (file.is_file() or file.name.endswith(".jfif")):
        continue
    analyzeResult = main.analyze.face(file.path)
    if analyzeResult:
        ageStart = math.floor(analyzeResult.get("age") / 10) * 10
        ageEnd = ageStart + 10
        ageRegion = str(ageStart) + "-" + str(ageEnd)
        gender = analyzeResult.get("gender")
        destinationPath = os.path.join("output/categorized-faces",gender,ageRegion)
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)
        shutil.move(file.path,destinationPath + "/" + file.name)
    else:
        shutil.move(file.path,"output/categorized-faces/NoCategory/" + file.name)