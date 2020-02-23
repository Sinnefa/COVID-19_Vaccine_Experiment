# Author: Alberto Calderone, Ph.D. - sinnefa@gmail.com

# Vaccines
# http://www.violinet.org/violinml/index.php

# Viral proteins sequences
# https://www.ncbi.nlm.nih.gov/search/api/download-sequence/?db=protein&id=NP_604433.1

# Virus sequences
# https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=10239&sort=taxonomy

# Proteoms
# https://www.uniprot.org/uniprot/?query=taxonomy:10508%20reviewed:yes&format=fasta&force=true&sort=score


import re
import urllib

base = "http://www.violinet.org/"
regex = r"<a href=\"(.*?)\".*?>(.*?)</a>" # regex to extract virus
regex2 = r">>[A-Z].*?\n(.*?)<" # regex to extract fasta
regex3 = r"styleLeftColumn2.*?[0-9+]\. (.*?)<\/span>" # regex to extract vaccine name

request = urllib.urlopen(base+"violinml/index.php")
text = ""
for source_line in request:
	text = text + source_line

matches = re.finditer(regex, text, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
	if "virus" not in match.group(2).lower():
		continue
	url = base+match.group(1).replace("../","")
	request = urllib.urlopen(url)
	text2 = ""
	for source_line in request:
        	text2 = text2 + source_line
	#if "human" not in text2.lower():
        #        continue
	matches2 = re.finditer(regex2, text2, re.MULTILINE | re.DOTALL)
	seq = ""
	for matchNum2, match2 in enumerate(matches2, start=1):
		seq = seq + match2.group(1)

	matches3 = re.finditer(regex3, text2, re.MULTILINE | re.DOTALL)
        vacs = []
        for matchNum3, match3 in enumerate(matches3, start=1):
                vacs.append(match3.group(1).strip())

	n = (" OR ".join(vacs)).strip()
	if len(seq)>0 and len(n)>0:
		print(n+"\t"+match.group(2)+"\t"+seq.replace("\n",""))
