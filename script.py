import requests
import re

def printSourceCode(url):
    print("\nSource Code:")
    sourceCode = getSourceCode(url)
    print(sourceCode)

def printCommunicationProtoclsLinks(url):
    print("\nCommunication Protocol Links:")
    sourceCode = getSourceCode(url)
    http = re.findall("http:", sourceCode)
    https = re.findall("https:", sourceCode)
    numOfHttp = len(http)
    numOfHttps = len(https)
    print("Number of http links: ", numOfHttp)
    print("Number of https links: ", numOfHttps)

def printURLs(url):
    print("\nURLs:")
    sourceCode = getSourceCode(url)
    urls = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", sourceCode)
    tlds = []
    for x, element in enumerate(urls):
        tld = urls[x].rsplit(".", 1)[1]
        tlds.append(tld)
    tlds = list(set(tlds))
    for x, element in enumerate(tlds):
        print(x + 1, ":", tlds[x])

def printHostnames(url):
    print("\nHostnames:")
    sourceCode = getSourceCode(url)
    urls = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", sourceCode)
    hostnames = []
    for x, element in enumerate(urls):
        hostname = urls[x].rsplit("//", 1)[1]
        hostnames.append(hostname)
    hostnames = list(set(hostnames))
    for x, element in enumerate(hostnames):
        print(x + 1, ":", hostnames[x])

def printHTMLtags(url):
    print("\nHTML tags:")
    sourceCode = getSourceCode(url)
    htmlTags = re.findall("\</(.*?)\>", sourceCode)
    htmlTags = list(set(htmlTags))
    for x, element in enumerate(htmlTags):
        print(x + 1, ":", "<" + format(htmlTags[x]) + ">")

def printTitles(url):
    print("\nTitles:")
    sourceCode = getSourceCode(url)
    urls = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", sourceCode)
    urls = list(set(urls))
    for x, element in enumerate(urls):
        sourceCode = getSourceCode(element)
        title = re.search("((?<=<title>)(.*?)(?=</title>))", sourceCode, re.DOTALL | re.IGNORECASE)
        if title:
            print(title.group(0))
        else:
            print("-- No title available --")

def getSourceCode(url):
    req = requests.get(url)
    sourceCode = req.text
    return sourceCode

if __name__ == "__main__":
    url = input("Insert URL: ")
    printSourceCode(url)
    printCommunicationProtoclsLinks(url)
    printURLs(url)
    printHostnames(url)
    printHTMLtags(url)
    printTitles(url)