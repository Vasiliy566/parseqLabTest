
def findMatches:
	ss = []
	info = []
	f = open('data/sequences.txt', 'r')
	data = ""
	f_ = f.readlines()[1:]
	for l in f_:
		if l[0] == ">":
			ss.append(data)
			info.append(l[14:-1].split("-"))
			data = ""
		else:
			data += l

	matches = []

	for i in range(len(ss)):
		for j in range(i + 1, len(ss)):
			if ss[i] == ss[j]:
				if info[i] != info[j]:
					matches.append([info[i], info[j]])
					print(ss[i] + " <> " + ss[j])
				

	output = []
	for x in matches:
	    if x not in output:
	        output.append(x)
	matches = output
	f.close()

	return matches
def printResult(matches):
	usless = []
	useful = []
	f = open("data/descripted_target.bed")
	for l in f:
		if len(l.split("\t")) == 6:
			usless.append([l.split("\t")[1], l.split("\t")[2]])
		elif len(l.split("\t")) == 7 or len(l.split("\t")) == 4: # for parts without extra information
			useful.append([l.split("\t")[1], l.split("\t")[2]])
		else:
			print("ERROR with gen length in descripted.bed file!")

	for pair in matches:
		type0 = "-1"
		type1 = "-1"
		if pair[0] in usless:
			type0 = "usless" # no dicription
		elif pair[0] in useful:
			type0 = "useful" # have discription in annotation file
		else:
			print("ERROR with determination of usles/usfull type 0")

		if pair[1] in usless:
			type1 = "usless"
		elif pair[1] in useful:
			type1 = "useful"
		else:
			print("ERROR with determination of usles/usfull type 1")
		if type1 != type0:	
			print("[{},{}] {} match with [{},{}] {} ".format(pair[0][0], pair[0][1], type0, pair[1][0], pair[1][1], type1))

matches = findMatches()
printResult(matches)

