# A simple motif search code that I wrote during my master's during my introduction to computaional biology

print('Motif Search')
print('------------')

#gathering inputs
f = str(input("Input fasta file: "))
m = str(input("Motif: "))
s = int(input("Relaxed percentage similarity: "))


# preparing inputs
file = open(f,'r')
content = file.readlines()
file.close()

genome = ""
motif = m
motifSize = len(motif)
similarity = int(s)/100

def searchForMotif(genome):

    si = 0

    result = ['#','\t','Location','\t','Motif','\t','Similarity %','\n']

    for baseID,base in enumerate(genome):

    
        end = baseID + motifSize

        unkMotif = ""

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

            result += [str(si),'\t',str(baseID + 1),'\t',str(unkMotif),'\t',str(percSimilarity),'\n']

    
    print('Done')
    return result



def resultFile(data):

    newData = ''.join(data)
    result = open('result.txt','w')
    result.write(newData)
    print('Data saved as \'result.txt\' file.\n')


for line in content[1::]:

    newArr = ""

    for el in line:

        if el == '\n':
            continue
        else:
            newArr += el

    genome += newArr


# finding similar motifs
result = searchForMotif(genome)

#saving result as result.txt file
resultFile(result)
