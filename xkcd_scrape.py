import urllib
import urllib2

pathToSaveTo = "/Users/broderickcarlin/Desktop/xkcd/"

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
