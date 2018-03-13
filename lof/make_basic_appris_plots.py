# -*- coding: utf-8 -*-
"""
task is to collect each gene id and record if it has a principal transcript of any level
"""

from collections import defaultdict

#overadvanced but useful for future
gene_iso =defaultdict(list)

gids_with_princ = set([])
gids_without_princ =set([])

ifile = "/home/jon/Downloads/appris_data.principal.txt"


for line in open(ifile):
    vals=line.split("\t")
    #print (vals)
    gid = vals[1]
    iso_class= vals[4]
    
    if iso_class.startswith("PRINCIPAL"):
        gids_with_princ.add(gid)
    else:
        gids_without_princ.add(gid)        

print ("with princ", len(gids_with_princ))
print ("without princ", len(gids_without_princ - gids_with_princ))
        
    


