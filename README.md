
## Canonical_transcript

    1.life平台对于经典转录本的定义https://ionreporter.thermofisher.com/ionreporter/help/GUID-A5502535-2C81-46FD-93C2-50FCB1F02CFD.html

    2.ACMG 推荐的经典转录本，但是目前数量只涉及到1000多个基因http://www.lrg-sequence.org

    3.一般一个基因对应多个经典转录本，为了寻求出现频次最多的哪一个，可实现的方法是对clinvar数据库中的转录本按照频次进行排序，排名最靠前默认为经典转录本:clinvar_canonical_transcript.txt、(No_verison)clinvar_canonical_trans.txt

    4.针对具体的突变，clinvar也会对应很多转录本注释信息，但是最主要的注释可参考文件：clinvar.out
    
    5.对clinvar数据库中的变异位点进行注释进行爬取，爬虫程序为：clinvar.py
    
    6.MSK.txt经典转录本是FDA批准的MSK的经典转录本，与clinvar的结果还是有些不同的建议首先这个文件