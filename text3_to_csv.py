import pandas as pd

data = [{'time': 2000, 'sector': 'sub', 'salary_month': 100000, 'salary_year': 2000000, 'worktime': 40, 'hourly_wage': 1500, 'job_title': 'eng', 'company': '202', 'over_time': 0 }]
df = pd.DataFrame(data)

textfile = []


with open('web_detail3.txt', encoding= 'utf-8', errors='ignore') as f:
	lines = f.readlines()
	# print(len(lines))
	for i in range(0, len(lines)):
		# if i%50 == 0:
		# 	continue
		work_our_wage = 0
		time = (lines[i][lines[i].find('year')+6:lines[i].find('year') + 10])
		# print((lines[i][lines[i].find('year')+6:lines[i].find('year') + 10]))
		sector_st = lines[i].find('sector')+9
		sector_end = lines[i].find(',', sector_st)-1

		sector = lines[i][sector_st: sector_end]
		# print(lines[i][sector_st: sector_end])

		salary_st = lines[i].find('type"')
		# print(salary_st)
		if salary_st == -1:
			ms = ys = 0
		else:
			if lines[i][salary_st + 7] == 'm':
				amount_st = lines[i].find('amount') + 8
				amount_end = lines[i].find('}',amount_st)

				ms = (lines[i][amount_st: amount_end])
				ys = 0
			elif lines[i][salary_st + 7] == 'y':
				amount_st = lines[i].find('amount') + 8
				amount_end = lines[i].find('}',amount_st)
				ms = 0
				ys = lines[i][amount_st: amount_end]
			else:
				# print('amount_zero')
				ys = ms = 0


		work_time_st = lines[i].find('week_work_time')+16
		if work_time_st == 15:
			work_time = 0
		else:
			work_time_end = lines[i].find(',',work_time_st)
			work_time = lines[i][work_time_st: work_time_end]
			# print(work_time)
			if work_time == 'null':
				work_time = 0

		
		work_hour_wage_st = lines[i].find('hourly_wage')+13
		if work_hour_wage_st == 12:
			work_hour_wage = 0
		else:
			work_hour_wage_end = lines[i].find(',',work_hour_wage_st)
			work_hour_wage = lines[i][work_hour_wage_st: work_hour_wage_end]

		if work_hour_wage == 'null':
			work_hour_wage = 0
		job_title_st = lines[i].find('job_title', lines[i].find('week_work_time'))+20
		job_title_end = lines[i].find('}',job_title_st)-1
		job_title = lines[i][job_title_st: job_title_end]
		# print(lines[i][job_title_st: job_title_end])

		company_st = lines[i].find('company')+18
		company_end = lines[i].find('}',company_st)-1
		company = lines[i][company_st: company_end]
		# print(lines[i][company_st: company_end])

		over_time_st = lines[i].find('overtime_frequency')+20
		if over_time_st == 19:
			over_time_st = -1
		else:
			over_time_end = over_time_st+1
			over_time = lines[i][over_time_st: over_time_end]
		if over_time == 'n':
			over_time = -1

		df = df.append(pd.DataFrame([{'time': time,
		'sector': sector,
		'salary_month': ms,
		'salary_year': ys,
		'worktime': float(work_time),
		'hourly_wage': float(work_hour_wage),
		'job_title': job_title,
		'company': company,
		'over_time': int(over_time)}]))

# useful information
df.to_csv('salary_wage_company.csv', encoding='utf-8-sig', index=False)