import requests,os
from zipfile import ZipFile


def download_file(url,filename):
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		with open(filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)

def extract(filename):
	with ZipFile(filename, 'r') as zip:
		zip.extractall('f')
	os.remove(filename)
    

def activate():
	pass

filename = 'kms.zip'
url = 'https://github.com/indrajith69/office365-activation/raw/main/KMS.zip'
download_file(url,filename)
extract(filename)