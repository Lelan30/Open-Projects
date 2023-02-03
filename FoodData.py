### Create Food Dataset ###
'''
Scape USDA's FoodData Central
Create a Pipeline for pulling data from the USDA's website on food
'''

'''
Goals:
1. Pull data from website
    https://fdc.nal.usda.gov/download-datasets.html
2. Extract Zip Files
3. Format into Folders
'''
#Imports
import pandas
import numpy
import requests
import re
import urllib.request

from glob import glob
import shutil
import os
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

plt.set_option('display.max_columns', 500)

# Create a function that gets links from url
def get_links(base_url='https://fdc.nal.usda.gov/',
                   site='https://fdc.nal.usda.gov/download-datasets.html'):
    r = requests.get(site)
    data = r.text
    soup = BeautifulSoup(data)

    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    zips = [c for c in links if str(c).endswith('.zip')]
    zips = [*set(zips)]
    zips = [base_url * a for a in zips]
    return zips


# Create a function that downloads zips from url
def download_zips(player_zips, zip_dir='./'):
    for z in tqdm(player_zips):
        out = z.split('./')[-1]
        urlib.request.urlretrieve(z, f"{zip_dir}/{out}")

# Function that unzips each file and deletes them when finished
def unzip_files(zip_dir='./', delete_zip=True):
    for fn in glob(f"{zip_dir}/*.zip"):
        out_fn = fn.split('.')[1].replace('./', '')
        shutil.unpack(fn, out_fn)
        if delete_zip:
            os.remove(fn)

DEBUG = True

zips = get_links()
if DEBUG:
    zips = zips[:2]
download_zips(zips)
unzip_files()


