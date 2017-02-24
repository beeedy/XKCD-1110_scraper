import urllib
import urllib2
import os
import shutil
from PIL import Image

pathToSaveTo = "xkcd/"
width = 147456
height = 65536

def scrape_images():
    if not os.path.exists(pathToSaveTo):
        os.makedirs(pathToSaveTo)

    for n in range(0,40):
        for e in range(0,40):
            try:
                urllib2.urlopen('http://imgs.xkcd.com/clickdrag/{:}n{:}e.png'.format(n,e))
            except:
                continue
            else:
                urllib.urlretrieve('http://imgs.xkcd.com/clickdrag/{:}n{:}e.png'.format(n,e), pathToSaveTo + "{:}_{:}.png".format(n,e))

        for w in range(0,40):
            try:
                urllib2.urlopen('http://imgs.xkcd.com/clickdrag/{:}n{:}w.png'.format(n,w))
            except:
                continue
            else:
                urllib.urlretrieve('http://imgs.xkcd.com/clickdrag/{:}n{:}w.png'.format(n,w), pathToSaveTo + "{:}_{:}.png".format(n,-1*w))

    for s in range(0,40):
        for e in range(0,40):
            try:
                urllib2.urlopen('http://imgs.xkcd.com/clickdrag/{:}s{:}e.png'.format(s,e))
            except:
                continue
            else:
                urllib.urlretrieve('http://imgs.xkcd.com/clickdrag/{:}s{:}e.png'.format(s,e), pathToSaveTo + "{:}_{:}.png".format(-1*s,e))

        for w in range(0,40):
            try:
                urllib2.urlopen('http://imgs.xkcd.com/clickdrag/{:}s{:}w.png'.format(s,w))
            except: 
                continue
            else:
                urllib.urlretrieve('http://imgs.xkcd.com/clickdrag/{:}s{:}w.png'.format(s,w), pathToSaveTo + "{:}_{:}.png".format(-1*s,-1*w))


def stitch_images():
    blank_image = Image.new("L", (width, height),0)
    sky_image = Image.new("L",(width,26624),255)

    blank_image.paste(sky_image, (0,0))

    count = 0
    total = 0

    for picture_name in os.listdir(pathToSaveTo): 
        total += 1
        try:
            cur_image = Image.open(pathToSaveTo + picture_name)
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

    blank_image.save('xkcdAll.png');


if __name__ == "__main__":
    #scrape_images()
    #stitch_images()
    shutil.rmtree(pathToSaveTo, ignore_errors=True, onerror=None)
    print("Completed!")