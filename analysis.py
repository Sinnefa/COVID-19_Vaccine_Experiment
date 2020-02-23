# Author: Alberto Calderone, Ph.D. - sinnefa@gmail.com

import sys
import pandas as pd
import numpy as np; import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from math import sqrt

def zify(some_dict):
	arr = some_dict.values()
	sum_sq = x_bar = 0
	for i, val in enumerate(arr):
		x_bar += val
		sum_sq += val * val
	n = 1 + i
	x_bar *= 1.0/n
	std = sqrt(1.0/i * sum_sq - (float(n) / i) * x_bar * x_bar)
	return {k:(v - x_bar)/std for k,v in some_dict.iteritems()}


# Counting every 3-gram with a sliding window
def countNgrams(s,name):
	res = {}
	for i in range(0,len(s)-2):
		k = s[i:i+3]
		if k not in res:
			res[k] = 0
		res[k] = res[k]+1
	l = pd.DataFrame([res],columns=res.keys(),index=[name])
	return l

d = pd.DataFrame() # Dataframe to hold all values

# Loading up COVID-19 sequence
file = open(sys.argv[2]).readlines()
r = countNgrams(file[0],"COVID-19")
d = d.append(r).fillna(0)

# Loading all vaccines sequences
file = open(sys.argv[1])
names = []
names.append("COVID-19")
count = 0
for l in file:
	count = count + 1
	#if count == 10: # Test purpose, limiting sequences
	#	break
	parts = l.split("\t")
	r = countNgrams(parts[2],parts[0])
	names.append(parts[0])
	d = d.append(r).fillna(0)

# Calculatin similary ignoring cmponents magnitue
scores = cosine_similarity(d)[0,]
sim = {}
for i in range(1,len(scores)):
	sim[names[i]]=scores[i]

simz = zify(sim)
# sortin and printing
sim = sorted(sim.items(), key=lambda x: x[1], reverse=True)
for i in sim:
	print(i[0]+"\t"+str(i[1])+"\t"+str(simz[i[0]]))

