import os
import pathlib
import shutil

from download_file import download_file
from unzip import unzip_all_files

if __name__ == '__main__':
	os.mkdir("temp")
	download_file(filename = "hello.zip", directory="temp")
	unzip_all_files("temp")
	shutil.rmtree("temp")
