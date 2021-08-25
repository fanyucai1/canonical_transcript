map,line={},""
infile=open("MSK.txt","r")
for line in infile:
    line=line.strip()
    map[line.split(",")[0]]=line.split(",")[1]
    print("%s,%s"%(line.split(",")[0],line.split(",")[1]))
infile.close()

infile=open("/Users/fanyucai/Downloads/MANE.GRCh38.v0.95.select_ensembl_genomic.gff","r")#https://ftp.ncbi.nlm.nih.gov/refseq/MANE/MANE_human/current/
for line in infile:
    line=line.strip()
    if not line.startswith("#") and line.split("\t")[2]=="transcript":
        array=line.split(";")
        gene_name, transript = "", ""
        for i in range(0,len(array)):
            if array[i].startswith('gene_name'):
                gene_name=array[i].split("=")[1]
            if array[i].startswith('Dbxref=RefSeq:'):
                transript=array[i].split(':')[1].split('.')[0]
        if not gene_name in map:
            map[gene_name]=transript
            print("%s,%s"%(gene_name,transript))
infile.close()
