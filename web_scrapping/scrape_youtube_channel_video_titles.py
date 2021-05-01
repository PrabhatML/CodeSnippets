'''
Using request
Using BS4
Using os
Using IO
'''
import requests
from bs4 import BeautifulSoup
import os
from fnmatch import fnmatch
import urllib
import time

# Settings
UPDATE_FILE_HOUR = 2

# Find page source if available
def find_page(url_name):
    for path,directories,files in os.walk(os.getcwd()):
        for file in files:
            if fnmatch(file,url_name):
                file_path = os.path.join(path,file)
                creation_time = ((time.time() - os.path.getctime(file_path)))/(3600)
                print(creation_time)
                if creation_time > UPDATE_FILE_HOUR:
                    os.remove(file_path)
                    return False 
                return file_path
    return False

# Get the soup from cache or actual page
def get_soup(url):
    url_name = urllib.parse.quote_plus(url) + ".html"
    url_name_location = find_page(url_name)
    if url_name_location:
        with open(url_name_location,'r') as f:
            soup = f.read()
    else:
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html5lib').prettify()
        with open('web_scrapping/output/'+url_name,'w') as f:
            f.write(soup)
    return soup

soup = get_soup("https://www.youtube.com/c/Programiz-studios/search?query=python")

