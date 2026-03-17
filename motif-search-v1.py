# A simple motif search code that I wrote during my master's during my introduction to computaional biology

import argparse
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="input fasta file", required=True)
parser.add_argument("-m","--motif", type=str, required=True)
parser.add_argument("-s","--sim", type=str, help="percentage similarity", default=100)

args = parser.parse_args()

print('Locating Motifs')

#gathering inputs
f = args.inp
m = args.motif
s = args.sim


# preparing inputs
file = open(f,'r')
content = file.readlines()
file.close()

genome = []
motif = list(m)
motifSize = len(motif)
similarity = int(s)/100

def searchForMotif(genome):

    si = 0

    result = ['#','\t','Location','\t','Motif','\t','Similarity %','\n']

    for baseID,base in enumerate(genome):

    
        end = baseID + motifSize

        unkMotif = []

        similar = motifSize

        for unkBaseID,unkBase in enumerate(genome[baseID:end]):

            if unkBase == motif[unkBaseID]:

                unkMotif += unkBase

            else:

                similar -= 1

                unkMotif += unkBase




        if (similar >= similarity * motifSize) and (len(unkMotif) == motifSize):

            si += 1
            percSimilarity = int((similar/motifSize)*100)

            result += [str(si),'\t',str(baseID + 1),'\t',str("".join(unkMotif)),'\t',str(percSimilarity),'\n']

    
    print('Done')
    return result



def resultFile(data):

    newData = ''.join(data)
    result = open('result.txt','w')
    result.write(newData)
    print('Data saved as \'result.txt\' file.\n')


for line in content[1::]:

    newArr = []

    for el in line:

        if el == '\n':
            continue
        else:
            newArr.append(el)

    genome += newArr


# finding similar motifs
result = searchForMotif(genome)

#saving result as result.txt file
resultFile(result)
