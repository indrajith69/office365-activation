import requests,os,time,shutil
from zipfile import ZipFile


def download_file(url,filename):
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		with open(filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)

def extract(filename):
	with ZipFile(filename, 'r') as zip:
		zip.extractall()
	os.remove(filename)
    

def activate():
	os.chdir('KMS')
	os.system('Activate.cmd /u')
	os.chdir('../')
	shutil.rmtree('KMS')
	print('done!\nexiting in 10 seconds...')
	time.sleep(10)

filename = 'kms.zip'
url = 'https://github.com/indrajith69/office365-activation/raw/main/KMS.zip'

try:
	download_file(url,filename)
	extract(filename)
	activate()
except:
	print('something went wrong! try again.\n(please make sure your connected to the internet)')
	time.sleep(10)