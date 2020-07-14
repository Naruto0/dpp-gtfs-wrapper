import os
import shutil
import tempfile
import zipfile
from typing import IO

from backend.settings import Config


EXPRESSION = "na znamení od 20 do 4 h,v SO a NE celodenně"


def zipdir(path: str, ziph: zipfile.ZipFile) -> None:
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), arcname=file)


def check_expression(file_in: IO, file_out: IO, expression=EXPRESSION) -> None:
    for line in file_in:
        unicode = line.decode("UTF-8")
        if expression in unicode:
            unicode = unicode.replace(expression, f'"{expression}"')
        file_out.write(unicode)


def update_file(zipname: str, filename: str) -> None:
    zip_dir = tempfile.mkdtemp()
    temp_text = os.path.join(zip_dir, filename)
    with zipfile.ZipFile(Config.ZIPFILE, "r") as z:
        with open(temp_text, "w", encoding="UTF-8") as out:
            with z.open(filename, "r") as s:
                check_expression(s, out)

        for item in z.infolist():
            if item.filename != filename:
                z.extract(item.filename, zip_dir)

    os.remove(zipname)

    zf = zipfile.ZipFile(zipname, "w", compression=zipfile.ZIP_DEFLATED)
    zipdir(zip_dir, zf)
    zf.close()

    shutil.rmtree(zip_dir)


def run_check():
    update_file(Config.ZIPFILE, "stops.txt")


if __name__ == "__main__":
    run_check()
