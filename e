def download_file(url,local_filename):
	a  = 0
	with requests.get(url, stream=True) as r:
		total_length = r.headers['Content-length']
		r.raise_for_status()
		with open(local_filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
				a+=len(chunk)
				print(a)




url = "https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1920_18MG.mp4"


download_file(url,'test.mp4')
