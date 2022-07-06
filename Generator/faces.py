import os
import time
import random
import main


while main.getDirSize("output") < 20000000000: # 20 GB
    randomName = None
    while (randomName == None) or (os.path.exists(randomName)):
        randomName = "output/faces/" + str(random.randint(10000000,99999999)) + ".jfif"
    print("Creating face with name: " + randomName)
    main.generate.face(randomName)
    time.sleep(1.5)