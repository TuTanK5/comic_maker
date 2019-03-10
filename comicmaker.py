import sys
import os
import argparse
import string

imgExt = ['.jpg', '.jpeg', '.png', '.bmp', '.webp']


def is_img(img):
    _, ext = os.path.splitext(img)
    if ext in imgExt:
        return True
    else:
        return False


def parse_dir(imgDir):
    fullpath = os.path.abspath(imgDir)
    items = os.listdir(fullpath)
    imgs = [os.path.join(fullpath, name) for name in items if is_img(os.path.join(fullpath, name))]

    if len(imgs) > 0:
        comicFileName = os.path.join(imgDir, 'comic.html')
        sitefile = open(comicFileName, "w+")
        print('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Comic</title></head><body>',
              file=sitefile)
        print("<h1>{}</h1>".format(os.path.basename(imgDir)), file=sitefile)
        for name in imgs:
            print('<img style="width: 100%; height: auto" src="{}"/>'.format(name.replace("\\\\", "/").
                                                                                replace("\\", "/")), file=sitefile)

        print('</body></html>', file=sitefile)
        sitefile.close()
        os.startfile(comicFileName, "open")

    for name in items:
        fullname = os.path.join(fullpath, name)
        if os.path.isdir(fullname):
            parse_dir(fullname)



def main():
    handler = argparse.ArgumentParser()
    handler.add_argument('dir')

    flags = handler.parse_args()

    parse_dir(flags.dir)


if __name__ == '__main__':
    main()