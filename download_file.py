import requests

def download_file(filename):
	base_url = "http://127.0.0.1:5000/uploads/"
	filename = filename
	url_to_download = f"{base_url}{filename}"
	file = requests.get(url_to_download).content
	with open("hello.txt", "wb") as f:
		f.write(file)
		print("got here")


if __name__ == '__main__':
	download_file("hello.txt")