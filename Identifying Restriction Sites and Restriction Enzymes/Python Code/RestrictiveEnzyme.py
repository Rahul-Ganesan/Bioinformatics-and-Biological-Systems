#This is program to create the table of Restrictive enzymes
import re
import pandas as pd

def readseq(filename):
    #Reading a Sequence from a file containg Sequence
    with open(filename, 'r') as f:

        seq = ''
        line = f.readline().rstrip()
        while line != '':
            seq += line
            line = f.readline().rstrip()

    return seq


def restriction_sites(seq, recog_seq):
    #Searching the indices of all restriction_sites in a sequence
    sites = []
    for site in re.finditer(recog_seq, seq):
        sites.append(site.start()+1)     #Storing The index of each restrictive Enzyme

    return sites


if __name__ == '__main__':
    seq=readseq("input.txt")  #Passing the file for Reading sequence

    
    # Storing Enzyme name and its recognition sequence in a dictionary
    
    name = {"GAATTC":"ECoRI","CCAGG":"EcoRII","CCTGG":"EcoRII","GGATCC":"BamHI","AAGCTT":"HindIII","TCGA":"TaqI","GCGGCCGC":"NotI","GANTC":"HinFI","GATC":"Sau3AI","CAGCTG":"PvuII*","CCCGGG":"SmaI","GGCC":"HaeIII","GACGC":"Hgal","AGCT":"Alul","GATATC":"EcoRV","CAGCAGN25NN":"EcoP151","GGTACC":"Kpnl","CTGCAG":"Pstl","GAGCTC":"Sacl","GTCGAC":"Sall","AGTACT":"Scal","ACTAGT":"Spel","GCATGC":"Sphl","AGGCCT":"Stul","TCTAGA":"Xbal"}       
    rec_seq_all = ["GAATTC","CCAGG","CCTGG","GGATCC","AAGCTT","TCGA","GCGGCCGC","GANTC","GATC","CAGCTG","CCCGGG","GGCC","GACGC","AGCT","GATATC","CAGCAGN25NN","GGTACC","CTGCAG","GAGCTC","GTCGAC","AGTACT","ACTAGT","GCATGC","AGGCCT","TCTAGA"]

    Table=dict()
    positions=list()
    noofcuts=list()
    enzymes=list()

    for n in rec_seq_all:
        Table[n]=restriction_sites(seq,n)
        positions.append(Table[n])
        noofcuts.append(len(Table[n]))
        enzymes.append(name[n])
        print(f"{name[n]}   {len(Table[n])}  {Table[n]} {n.lower()}")
    
    #exporting the output file in csv format
    
    
    data={'Enzyme Name':enzymes,'No. of cuts':noofcuts,'Positions Of sites':positions,'Recognition Sequence':rec_seq_all}

    Rtable=pd.DataFrame(data,columns=['Enzyme Name','No. of cuts','Positions Of sites','Recognition Sequence'])
    
    Rtable.to_csv("Sequence.csv")