from bs4 import BeautifulSoup
import os 
import requests

rootUrl = "http://univ.ency-education.com"
url = "http://univ.ency-education.com/5an_lessons-psychiatrie.html"

currentPath = os.getcwd()
path = "{currentpath}/Lectures".format(currentpath=currentPath)
os.mkdir(path)

page = requests.get(url)

linksFound = []

soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.find_all('a'):
    scrapedUrl = link.get('href')
    if (scrapedUrl[-3:] == "pdf" or scrapedUrl[-4:] == "pptx"):
        fullUrl = "{root}{url}".format(root= rootUrl, url=scrapedUrl)
        linksFound.append(fullUrl)
    else: 
        continue

if (len(linksFound) != 0) :
    answer = input("Found {numFiles} Files, Download ? [Y/n] ".format(numFiles= len(linksFound)))
    if (answer != 'n' or answer != 'N') :
        for file in linksFound : 
            commandToDownload = "wget -P {path} {lectureLink}".format(path=path, lectureLink=file)
            os.system(commandToDownload) 
