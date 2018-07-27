import json
import re
import requests
import sys

# you should use pip to install requests before running
# Example:
# python -m pip install requests
# download function
def DownloadFile(url, name):
    with open(name, "wb") as code:
        code.write(requests.get(url).content)

def DownloadAnote(listpath=None):
    # Open response json file
    if None != listpath:
        listPath = listpath
    else:
        listPath = "path.json"

    with open(listPath,'r') as resp_f:
        jsonfile = json.load(resp_f)
    
    # Use data dict
    data = jsonfile["data"]
    
    # Download each image
    for path in data:
        # get link
        filelink = path["imgLink"]
        # get name
        filename = filelink.lstrip("https://storage.googleapis.com/app-anote/")
        # delete the code and fix the file extension
        fileregex = re.compile(r'_[0-9]*.png')
        filename  = fileregex.sub('.png',filename)
        # if the exif info shows the image is jpg, use code below.
        # filename = fileregex.sub('.jpg',filename)
        DownloadFile(filelink, filename)
    
    return True

DownloadAnote(sys.argv[1])