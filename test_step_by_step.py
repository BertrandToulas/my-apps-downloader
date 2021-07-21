'''For granular testing and inspection of urls (e.g. status code, content type,
urls contained within the page response...)'''
import os
import pathlib
import re

import requests
from bs4 import BeautifulSoup

import apps

directory = os.path.join('Desktop', 'installers')
download_path = os.path.join(pathlib.Path.home(), directory)
if not os.path.isdir(download_path):
    os.mkdir(download_path)
os.chdir(download_path)

program = apps.programs['insert_app_name']
page = program.download_page
pattern = program.pattern
direct = program.download_url
base = program.base_url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

# FOR HTML
s = requests.Session()
r_html = s.get(url=page)
print(type(r_html))
print(r_html.status_code)
print(r_html.headers)
print(r_html.headers['Content-Type'])
print(r_html.url)
html = r_html.text
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
anchors = soup.select('a')
# [print(anchor) for anchor in anchors]
links = [link.get('href') for link in anchors
         if isinstance(link.get('href'), str)]
# [print(link) for link in links]
versions = [version for version in links
            if pattern.search(version) != None]
latest = versions[0]
if base == None:
    direct = latest
elif base != None:
    direct = base + latest
file_name = direct.split('/')[-1]
# print(file_name)
file_bytes = r_html.get(direct).content
with open(file_name, 'wb') as output_file:
    output_file.write(file_bytes)

# FOR JSON
# s = requests.Session()
# r_json = s.get(url=page)
# print(type(r_json))
# print(r_json.status_code)
# print(r_json.headers)
# print(r_json.headers['Content-Type'])
# print(r_json.url)
# json = page.json()
# json_list = json['products']
# links = [link['url'] for link in json_list]
# versions = [version for version in links if pattern.search(version) != None]
# latest_version = versions[0]
# direct = latest_version
# file_name = direct.split('/')[-1]
# file_bytes = r_json.get(direct).content
# with open(file_name, 'wb') as output_file:
#     output_file.write(file_bytes)