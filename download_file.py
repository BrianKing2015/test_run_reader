import requests
import pathlib

def download_file(filename, directory):
	base_url = "http://127.0.0.1:5000/uploads/"
	filename = filename
	url_to_download = f"{base_url}{filename}"
	file = requests.get(url_to_download).content
	to_save = pathlib.Path(directory, filename)
	with open(to_save, "wb") as f:
		f.write(file)


if __name__ == '__main__':
	download_file(filename = "hello.zip", directory="temp")
