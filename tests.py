from annotator import getChromosomeTarget, getCoordinatesTarget, getChromosomeAnn, getCoordinatesAnn, getGeneAnn
def tests(debug):
	#target panel tests
	print("TEST :\n", "*"*20)
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
	gene = "gene-DAXX"
	print(getChromosomeAnn(gen) == chrom)
	print(getCoordinatesAnn(gen) == coord)
	print(getGeneAnn(gen) == gene)
	if(debug):
		print("Annotation:")
		print(getChromosomeAnn(gen))
		print(getCoordinatesAnn(gen))
		print(getGeneAnn(gen))
	print("*"*20)
debug = False
tests(debug)