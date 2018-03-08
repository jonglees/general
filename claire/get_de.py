"""Prits out a list of differentially expressed genes"""
import os
import csv
import gzip
id_map = {}
import sys

cut_off = float(sys.argv[1])
for line in gzip.open(os.path.expanduser(os.path.join("~","Dropbox/CLAIRE/uniprot_map.gz"))):
    cols =  line.split("\t")
    id_map[cols[0]] = cols[2]

for c,line in enumerate(csv.reader(open(os.path.expanduser(os.path.join("~","Dropbox/CLAIRE/all_sig.csv"))))):
    if c ==0: continue
    fc = float(line[-2])
    up = id_map.get(line[0])
    if up is None: continue
    if cut_off ==0: print up
    if cut_off > 0 and fc > cut_off: print up
    if cut_off < 0 and fc < cut_off: print up

