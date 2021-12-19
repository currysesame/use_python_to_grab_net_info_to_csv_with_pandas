import pandas as pd


# df = df.append(pd.DataFrame([{'time': (lines[i][lines[i].find('year')+6:lines[i].find('year') + 10]),
# 'sector': lines[i][sector_st: sector_end],
# 'salary_month': ms, 'salary_year': ys,
# 'worktime': float(work_time),
# 'hourly_wage': float(work_hour_wage),
# 'job_title': lines[i][job_title_st: job_title_end],
# 'company': lines[i][company_st: company_end],
# 'over_time': int(over_time)}]))




df = pd.read_csv('salary_wage_company.csv')

print(df)

# recent info
filt = df['time'] >= 2018
df_recent = df[filt]
print(df_recent)

# no need to stay outside late
filt = df_recent['worktime'] < 41.1
df_work_free_time =df_recent[filt]
print(df_work_free_time)

# filt out something weird
filt = df_work_free_time['worktime'] > 31
df_work_free_time2 =df_work_free_time[filt]
print(df_work_free_time2)

# good pay
filt = df_recent['hourly_wage'] > 480
df_worth =df_work_free_time2[filt]
print(df_worth)

# not hard work frequently
filt = df_recent['over_time'] <=1
df_health =df_worth[filt]
print(df_health)

# filt = df_recent['salary_month'] > 60000
# df_worth =df_worth[filt]
# print(df_worth)


df_health.to_csv('salary_wage_company_bad.csv', encoding='utf-8-sig', index=False)