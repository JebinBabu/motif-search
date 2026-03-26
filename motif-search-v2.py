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


chromosomes = []
chromosome_ids = []


# Reading genome file 

with open(args.inp, 'r') as genome_file:

    new_chromososme = []

    while True:

        line = genome_file.readline()[:-1]

        if len(line) == 0:
            break
        
        if '>' in line:

            chrom_head = line.split(' ')[0][1:]
            chromosome_ids.append(chrom_head)
            
            if len(new_chromososme) > 0:

                chromosomes.append(new_chromososme)
                new_chromososme = []

        else:

            new_chromososme += list(line)

    chromosomes.append(new_chromososme)
    new_chromososme = []




def searchForMotif(chromosome, chromosome_id):

    si = 0

    for baseID,base in enumerate(chromosome):

    
        end = baseID + motifSize

        unkMotif = []

        similar = motifSize

        for unkBaseID,unkBase in enumerate(chromosome[baseID:end]):

            if unkBase == motif[unkBaseID]:

                unkMotif += unkBase

            else:

                similar -= 1

                unkMotif += unkBase




        if (similar >= similarity * motifSize) and (len(unkMotif) == motifSize):

            si += 1
            percSimilarity = int((similar/motifSize)*100)

            result = f"{si}\t{chromosome_id}\t{baseID + 1}\t{args.motif}\t{("".join(unkMotif))}\t{motifSize-similar}\t{percSimilarity}\n"

            outfile.write(result)


# finding similar motifs

with open(args.out.replace("motif",args.motif),"w") as outfile:

    header = "#\tChromosome_ID\tLocation\tQuery\tMotif\tMismatches\tSimilarity %\n"
    outfile.write(header)

    for chromosome_id, chromosome in zip(chromosome_ids, chromosomes):

        searchForMotif(chromosome, chromosome_id)