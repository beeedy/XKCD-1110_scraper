from PIL import Image
import os

pathToSearchIn = "/Users/broderickcarlin/Desktop/xkcd/"

width = 147456
height = 65536

blank_image = Image.new("L", (width, height),0)
sky_image = Image.new("L",(width,26624),255)

blank_image.paste(sky_image, (0,0))

count = 0
total = 0

for picture_name in os.listdir(pathToSearchIn): 
    total += 1
    try:
        cur_image = Image.open(pathToSearchIn + picture_name)
    except:
        print "Error with file: " + picture_name
        count += 1
        continue
    [name, extension] = picture_name.split('.')
    [y, x] = name.split('_')
    x = int(x)
    y = int(y)
    if(y<0):
        y += 1
    if(x>0):
        x -= 1
    blank_image.paste(cur_image, (x*2048 + width/2 - 1024*6, y*-2048 + height/2 - 1024*6))

blank_image.save(pathToSearchIn + 'xkcdAll.png');
print "Completed!"
