import os
import zipfile
import pathlib

def unzip_all_files(directory):
	for file in os.listdir(directory):
		target_file = pathlib.Path(directory,file)
		if zipfile.is_zipfile(target_file):
			with zipfile.ZipFile(target_file) as item:
				name = pathlib.Path(item.filename).stem
				os.mkdir(name)
				item.extractall(path=name)

if __name__ == '__main__':
	unzip_all_files("uploads")