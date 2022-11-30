from PIL import Image
import random
from os import listdir

base_folder = "tier_list_bases/"

people_folder = "people/"

base_image = "lunch.png"

im = Image.open(base_folder + base_image)

peopleList = listdir(people_folder)
for i in range(1):
    im = Image.open(base_folder + base_image)
    for name in peopleList:

        x = random.randint(100,im.size[0]-100)
        y = random.randint(100,im.size[1]-100)

        peopleImage = Image.open(people_folder + name)
        peopleImage = peopleImage.resize((100,150))

        im.paste(peopleImage,(x,y))
    im.save("./tier_list.png", "PNG")
