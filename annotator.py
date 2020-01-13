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
#main functions
def findGenInAnn(): # genDescription from target
	descripted_target = open("descripted_target_forgotten.bed", "w+")
	target_f = open("forgotten.bed", 'r')
	target = target_f.readlines()[1:]
	for genDiscription in target:
		chrom = getChromosomeTarget(genDiscription)
		coord = getCoordinatesTarget(genDiscription)
		ann = open("GCF_000001405.39_GRCh38.p13_genomic.gff", "r")
		i = 0
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
#get gene ID from description
def getGenes():
	f = open("descripted_target.bed", 'r')
	genes = []
	for l in f:
		gen = getGeneAnn(l)
		if gen not in genes:
			if gen != -1:
				genes.append(gen)
	print(genes)
	
#def main():
#	debug = True
#	tests(debug)
#	findGenInAnn()
#	getGenes()
#main()