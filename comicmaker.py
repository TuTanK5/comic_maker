"""Generate html from image folder."""
import argparse
import webbrowser
from pathlib import Path

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]


def _is_img(img: Path) -> bool:
    if img.suffix in IMAGE_EXTENSIONS:
        return True
    return False


def parse_dir(img_dir: Path) -> None:
    """Parse image directory."""
    fullpath = Path(img_dir).resolve()
    items = fullpath.glob("**/*")
    imgs = [file for file in items if _is_img(file)]

    if len(imgs) > 0:
        comic_strip_file_name = fullpath/"comic.html"
        with open(comic_strip_file_name, "w+") as sitefile:
            print('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Comic</title></head><body>',
                file=sitefile)
            print(f"<h1>{fullpath.stem}</h1>", file=sitefile)
            for name in imgs:
                print(f'<img style="width: 100%; height: auto" src="file://{name}"/>', file=sitefile)
            print("</body></html>", file=sitefile)

        webbrowser.open(str(comic_strip_file_name))

    for fullname in items:
        if fullname.is_dir():
            parse_dir(fullname)



def _main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    flags = parser.parse_args()

    parse_dir(flags.dir)


if __name__ == "__main__":
    _main()
