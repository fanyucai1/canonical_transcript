import re
import requests
import os
from bs4 import BeautifulSoup
from multiprocessing import Pool
infile=open("variant_summary.txt","r")
varid={}
for line in infile:
    line=line.strip()
    if re.search(r'GRCh37',line):
        array=line.split("\t")
        varid[array[-1]]=array[2]
infile.close()

infile=open("clinvar.vcf","r")
pos,uid={},[]
for line in infile:
    line=line.strip()
    if not line.startswith("#"):
        array = line.split("\t")
        tmp=array[0]+"\t"+array[1]+"\t"+array[2]+"\t"+array[3]+"\t"+array[4]
        if array[2] in varid:
            pos[array[2]]=tmp
            uid.append(array[2])
download={}
if not os.path.exists("clinvar.out"):
    outfile = open("clinvar.out", "w")
    outfile.write("#Chr\tPOS\tID\tREF\tALT\tClinvar_anno\tClinvar_others\n")
    outfile.close()
else:
    infile=open("clinvar.out", "r")
    for line in infile:
        line=line.strip()
        array=line.split("\t")
        download[array[2]]=1
    infile.close()
def run(id):
    if not id in download:
        result=""
        html='https://www.ncbi.nlm.nih.gov/clinvar/variation/%s/'%(id)
        res = requests.get(html)
        ret = res.text
        soup = BeautifulSoup(ret, 'html.parser')
        tables=soup.find_all('table')
        for key in tables:
            if 'hgvstable' in key['class']:
                for td in key.find_all('td'):
                    if td.string and re.search(r'NM',td.string.strip()):
                        result+=td.string.strip()
                        result+=","
        outfile = open("clinvar.out", "a+")
        outfile.write("chr%s\t%s\t%s\n" % (pos["%s"%(id)], varid["%s"%(id)], result.strip(",")))
        outfile.close()

if __name__=="__main__":
    pool = Pool(processes=100)
    pool.map(run, uid)