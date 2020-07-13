import urllib.request as req
import os

def find_onset(str_index, index):
	if index > 9:
		if index < 100:
			onset = "0"
		else: 
			onset = ""
	else:
		 onset = "00" 
	return onset

def save_from_url(onset, index, url, path):
	
	opener = req.build_opener()
	opener.addheaders = [('User-agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")]
	req.install_opener(opener)

	req.urlretrieve(url, path)
	
	print("Saving to %s !" % path)
	
	return None

base_url = str(input("Enter base URL: "))
str_index = str(input("Starting from index (all digits): "))
index = int(str_index)
needs_onset = False if len(str_index) == len(str(index)) else True
endex = int(input("Ending at index: "))
extension = str(input("Enter file extension: "))
extension = extension.lower() if "." in extension else "." + extension.lower()
pathname = str(input("Enter saving directory path: "))

if not os.path.isdir(pathname):
	if pathname[-1] == "\\" :
		pathname = pathname[0:len(pathname) -1]
	os.mkdir(pathname)
	
if needs_onset:
	for i in range(index, endex+1):
		onset = find_onset(str_index, index)
		filename = onset + str(index) + extension
		url = base_url + filename
		fullpath = pathname + "\\" + filename
		save_from_url(onset, index,url, fullpath)
		index += 1
else:
	for i in range(index, endex+1):
		onset = ""
		filename = str(index) + extension
		url = base_url + filename
		fullpath = pathname + "\\" + filename
		save_from_url(onset, index,url, fullpath)
		index += 1