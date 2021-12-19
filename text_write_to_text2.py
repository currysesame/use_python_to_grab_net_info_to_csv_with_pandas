import  re

textfile = []


with open('web_detail.txt', encoding= 'utf-8', errors='ignore') as f:
	lines = f.readlines()
	print(len(lines))
	for i in range(0, len(lines)):
		# find the start pt that the info we want
		indexs = [m.start() for m in re.finditer('{"data_time":', lines[i])]
		if len(indexs) > 0:
			print(indexs[0])
			textfile.append(lines[i][82000:])

# Shrink down the info, write to the text.
with open('web_detail2.txt', 'w', encoding="utf-8") as f:
	for i in range(len(textfile)):
		f.write(textfile[i] + '\n')