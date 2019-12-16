import re

infile1=open("MSK.txt","r")
infile2=open("clinvar_canonical_trans.txt","r")

gene={}
for line in infile1:
    line=line.strip()
    array=re.split("\s",line)
    gene[array[0]]=array[1]
infile1.close()

for line in infile2:
    line = line.strip()
    array = re.split("\s", line)
    if array[0] in gene:
        tmp=array[1].split(".")
        if gene[array[0]]==tmp[0]:
            pass
        else:
            print(line)
    else:
        #print("%s not in panel"%(array[0]))
        pass
infile2.close()