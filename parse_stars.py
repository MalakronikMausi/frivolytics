import re

ranks = range(1,501)
names = []
urls = []
roles = []
ages = []

next_is_role = False
with open('starmeter.txt','r') as f:
	for line in f:	
		if next_is_role:
			roles.append(re.split('<|\s',line)[0])
			next_is_role = False
		elif line.find('<span class=\"display-name \">') > -1:
			goodies = (line.split('<span class=\"display-name \">'))[1].split('</span>')[0]
			names.append((goodies.split('>'))[1].split('<')[0])
			urls.append(goodies.split('\"')[1] + 'graph?ref_=nm_mtr')
		elif line.find('<span class=\"age_rank sort\">') > -1:
			ages.append((line.split('<span class=\"age_rank sort\">')[1]).strip())
		elif line.find('<li class="job_categories ellipsis">') > -1:
			next_is_role = True
		

with open('stars_out.csv','w') as f:
	f.write('rank,name,url,role,age\n')
	for n in range(500):
		f.write(','.join([str(ranks[n]),names[n],urls[n],roles[n],ages[n]]) + '\n')
			