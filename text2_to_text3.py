
textfile = []

# split each job info
with open('web_detail2.txt', encoding= 'utf-8', errors='ignore') as f:
	lines = f.readlines()
	# print(len(lines))
	for i in range(0, len(lines)):
		# print((lines[i]))
		fifty_jobs = lines[i].split('},{')
		for j in range(len(fifty_jobs)):
			# print(fifty_jobs[j])
			textfile.append(fifty_jobs[j])



with open('web_detail3.txt', 'w', encoding="utf-8") as f:
	for i in range(len(textfile)):
		f.write(textfile[i] + '\n')