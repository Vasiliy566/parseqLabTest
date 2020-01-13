#for target panel
def getChromosomeTarget(genDiscription):
	return(int(genDiscription.split()[0][3:5]))
def getCoordinatesTarget(genDiscription):
	return([int(genDiscription.split()[1]), int(genDiscription.split()[2])])
#for annotation file
def getChromosomeAnn(genDiscription):
	
	return(int(genDiscription[7:9] ))
def getCoordinatesAnn(genDiscription):
	return([int(genDiscription.split("\t")[3]), int(genDiscription.split("\t")[4])])

def getGeneAnn(genDiscription):
	start = genDiscription.find("ID=") + 2 # +1 besause next symbol is '=', len("gene") = 5
	end = genDiscription.find(";", start) # max number of chromosome int this case is [0, 100] 
	if len(genDiscription.split("\t")) == 6	:
		return -1
	return(genDiscription[start+1:end])

def findGenInAnn(): # genDescription from target
	descripted_target = open("data/descripted_target_forgotten.bed", "w+")
	target_f = open("data/IAD143293_241_Designed.bed", 'r')
	target = target_f.readlines()[1:]
	for genDiscription in target:
		chrom = getChromosomeTarget(genDiscription)
		coord = getCoordinatesTarget(genDiscription)
		ann = open("GCF_000001405.39_GRCh38.p13_genomic.gff", "r")
		written = False
		for l in ann: # must be boosted with binary search
			if l[0] != "#":
				
				match = ( (getChromosomeAnn(l) == chrom) and (getCoordinatesAnn(l)[0] <= coord[0]) and (getCoordinatesAnn(l)[1] >= coord[1]) and(l.split("\t")[2] != "region")) 
				if( match ):
					print(l.split("\t"))
					descripted_target.write(genDiscription + l.split("\t")[8] )
					descripted_target.flush()
					written = True

		if not written:
			descripted_target.write(genDiscription)
			descripted_target.flush()
			writen = True				
		ann.close()
	descripted_target.close()
	target.close()

def getGenes():
	f = open("data/descripted_target.bed", 'r')
	genes = []
	for l in f:
		gen = getGeneAnn(l)
		if gen not in genes:
			if gen != -1:
				genes.append(gen)
	print(genes)	
#simple tests
def tests(debug = False):
	#target panel tests
	print("TEST:\n", "*"*20)
	gen = "chr20	43059982	43060285	AMPL7154785562	.	Pool=2;SUBMITTED_REGION=AMPL7154783265,AMPL7154785561,AMPL7154785562"
	chrom = 20
	coord = [43059982, 43060285]

	print(getChromosomeTarget(gen) == chrom)
	print(getCoordinatesTarget(gen) == coord)

	if(debug):
		print("Target:")
		print(getChromosomeTarget(gen))
		print(getCoordinatesTarget(gen))
	#anootation tests
	gen = "NC_000006.12	BestRefSeq%2CGnomon	gene	33318558	33323016	.	-	.	ID=gene-DAXX;Dbxref=GeneID:1616,HGNC:HGNC:2681,MIM:603186;Name=DAXX;description=death domain associated protein;gbkey=Gene;gene=DAXX;gene_biotype=protein_coding;gene_synonym=BING2,DAP6,EAP1,SMIM40"
	chrom = 6
	coord = [33318558,	33323016]
	gene = "DAXX"

	print(getChromosomeAnn(gen) == chrom)
	print(getCoordinatesAnn(gen) == coord)
	print(getGeneAnn(gen) == gene)

	if(debug):
		print("Annotation:")
		print(getChromosomeAnn(gen))
		print(getCoordinatesAnn(gen))
		print(getGeneAnn(gen))
	print("*"*20)
def main():
	debug = True
	tests(debug)
	findGenInAnn()
	getGenes()
main()