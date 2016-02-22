#!/usr/bin/python

import re

fileToParse = open("tor-snort.txt","r")
compiledRegexSigContent = re.compile("\[([^)]+)\]")

rows = fileToParse.readlines()

cleared=[]

for item in rows:
    cleared.append(compiledRegexSigContent.findall(item))

ifade = ""
for i in cleared:
	for j in i:
        	d = j.split(",")
		for k in d:
       		    print k
 	

