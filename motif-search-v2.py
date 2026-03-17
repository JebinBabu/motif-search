import argparse
parser = argparse.ArgumentParser(description="A script to find motifs in a fasta file.")

parser.add_argument("-i","--inp", type=str, help="Input fasta file", required=True)
parser.add_argument("-m","--motif", type=str, help="Motif", required=True)
parser.add_argument("-p","--relax_perc", type=str, help="Relaxed percentage similarity", default=100)
parser.add_argument("-o","--out", type=str, help="Output file", default="motif_result.txt")

args = parser.parse_args()

print(f'Searching for {args.motif}\n')

#gathering inputs
f = args.inp
m = args.motif
s = args.relax_perc

motif = list(m)
motifSize = len(motif)
similarity = float(s)/100

chromosomes = {}
genome = []

# Reading genome file 

with open(args.inp, 'r') as genome_file:

    # chrom_head = ""
    # chrom = []

    while True:

        line = genome_file.readline()

        if len(line) == 0:
            break
        
        if '>' in line:

            chrom_head = line.split(' ')[0][1:]


        genome += list(line)



def searchForMotif(genome):

    with open(args.out.replace("motif",args.motif),"w") as outfile:
        si = 0

        header = "#\tLocation\tQuery\tMotif\tSimilarity %\n"

        outfile.write(header)

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

                result = f"{si}\t{baseID + 1}\t{args.motif}\t{("".join(unkMotif))}\t{percSimilarity}\n"

                outfile.write(result)


# finding similar motifs
searchForMotif(genome)