import requests

# the information that we want to grab.
page_init = 'https://www.goodjob.life/salary-work-times/latest?p='

with open('web_detail.txt', 'w', encoding = "utf-8") as f:
	for i in range(1,394):
		# save the text information
		page_request = requests.get(page_init + str(i))
		# write to text
		f.write(page_request.text + '\n')

