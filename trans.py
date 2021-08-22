import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-l","--list",help="gene list")
args=parser.parse_args()

map,line={},""
infile=open("MSK.txt","r")
for line in infile:
    line=line.strip()
    map[line.split()[0]]=line.split()[1]
infile.close()

infile=open("/Users/fanyucai/Desktop/MANE.GRCh38.v0.95.select_ensembl_genomic.gff","r")#https://ftp.ncbi.nlm.nih.gov/refseq/MANE/MANE_human/current/
gene_name,transript="",""
for line in infile:
    line=line.strip()
    if not line.startswith("#") and line.split("\t")[2]=="transcript":
        array=line.split(";")
        for i in range(0,len(array)):
            if array[i].startswith('gene_name'):
                gene_name=array[i].split("=")[1]
            if array[i].startswith('Dbxref=RefSeq:'):
                transript=array[i].split(':')[1].split('.')[0]
            if not gene_name in map:
                map[gene_name]=transript
infile.close()

infile=open(args.list,"r")
for line in infile:
    line=line.strip()
    print(map[line])
infile.close()