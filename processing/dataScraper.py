# #import urllib2  # the lib that handles the url stuff
# from urllib.request import urlopen
# data = urlopen("https://companiesmarketcap.com/energy/largest-companies-by-market-cap/")
# for line in data: # files are iterable
#     print(line)

#get necessary packages 
import pdb
from urllib.request import Request, urlopen
import re

#create request 
#(explain handshaking)
req = Request(
    url= 'https://companiesmarketcap.com/energy/largest-companies-by-market-cap/', 
    headers={'User-Agent': 'Mozilla/5.0'}
)

#get the text file of html
#(explain html basics and inspect method)
webpage = str(urlopen(req).read())

#split into array 
splitBySort = re.split("data-sort",webpage)

#get formula for how to access the correct one 
#either through analysis or through experimentation
#we know have a good subset 
splitBySort = splitBySort[3::4]

#now, we want to get the actual prices and numbers 
#use re.search example
#what we will use: $<digits>.<digits> 
#   ($\d+\.\d+)

data = []
for line in splitBySort:
    putInData = re.search( "\$\d+\.\d+",line)[0]
    data = data + [float(putInData[1:])]



