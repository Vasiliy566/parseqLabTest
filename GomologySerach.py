#part 2

#>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p13 Primary Assembly
import os

def getChromosomeTarget(genDiscription):
	return(int(genDiscription.split()[0][3:5]))
def getCoordinatesTarget(genDiscription):
	return([int(genDiscription.split()[1]), int(genDiscription.split()[2])])

chromes = [">NC_000001.11 Homo sapiens chromosome 1, GRCh38.p13 Primary Assembly",
">NC_000002.12 Homo sapiens chromosome 2, GRCh38.p13 Primary Assembly",
">NC_000003.12 Homo sapiens chromosome 3, GRCh38.p13 Primary Assembly",
">NC_000004.12 Homo sapiens chromosome 4, GRCh38.p13 Primary Assembly",
">NC_000005.10 Homo sapiens chromosome 5, GRCh38.p13 Primary Assembly",
">NC_000006.12 Homo sapiens chromosome 6, GRCh38.p13 Primary Assembly",
">NC_000007.14 Homo sapiens chromosome 7, GRCh38.p13 Primary Assembly",
">NC_000008.11 Homo sapiens chromosome 8, GRCh38.p13 Primary Assembly",
">NC_000009.12 Homo sapiens chromosome 9, GRCh38.p13 Primary Assembly",
">NC_000010.11 Homo sapiens chromosome 10, GRCh38.p13 Primary Assembly",
">NC_000011.10 Homo sapiens chromosome 11, GRCh38.p13 Primary Assembly",
">NC_000012.12 Homo sapiens chromosome 12, GRCh38.p13 Primary Assembly",
">NC_000013.11 Homo sapiens chromosome 13, GRCh38.p13 Primary Assembly",
">NC_000014.9 Homo sapiens chromosome 14, GRCh38.p13 Primary Assembly",
">NC_000015.10 Homo sapiens chromosome 15, GRCh38.p13 Primary Assembly",
">NC_000016.10 Homo sapiens chromosome 16, GRCh38.p13 Primary Assembly",
">NC_000017.11 Homo sapiens chromosome 17, GRCh38.p13 Primary Assembly",
">NC_000018.10 Homo sapiens chromosome 18, GRCh38.p13 Primary Assembly",
">NC_000019.10 Homo sapiens chromosome 19, GRCh38.p13 Primary Assembly",
">NC_000020.11 Homo sapiens chromosome 20, GRCh38.p13 Primary Assembly",
">NC_000021.9 Homo sapiens chromosome 21, GRCh38.p13 Primary Assembly",
">NC_000022.11 Homo sapiens chromosome 22, GRCh38.p13 Primary Assembly",
">NC_000023.11 Homo sapiens chromosome X, GRCh38.p13 Primary Assembly",
">NC_000024.10 Homo sapiens chromosome Y, GRCh38.p13 Primary Assembly"]

ref = open("data/GCF_000001405.39_GRCh38.p13_genomic.fna", 'r') #80 symbols in string
inp = open("results/discripted_target.bed", 'r')

for l in  inp:
	#print(l)
	chrom = chromes[getChromosomeTarget(l) - 1].split()[0]
	coord = getCoordinatesTarget(l)
	command = "samtools faidx GCF_000001405.39_GRCh38.p13_genomic.fna {}:{}-{} >> sequences.txt".format(chrom[1:], coord[0], coord[1]) 
	print(command)
	os.system(command)
