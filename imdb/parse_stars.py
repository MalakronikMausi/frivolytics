import re

ranks = range(1,1001)
names = []
urls = []
ages = []
heights = []
roles = []
titles = []
akas = []

next_is_role = False
next_is_titles = False
next_is_aka = False
found_aka = True
index = 0;
with open('starmeter.txt','r') as f:
	for line in f:	
		if next_is_role:
			roles.append(re.split('</li>',line)[0].replace('<span class="delimiter"> | </span>', '|').strip())
			next_is_role = False
		elif next_is_titles:
			title_list = []
			for title in line.split('<span class="delimiter"> | </span>'):
				goodies = title.split('<span class=\"display-title \">')[1].split('<span class="year">')[0]
				title_list.append(goodies.split('>')[1].split('<')[0])
			titles.append('|'.join(title_list))
			next_is_titles = False
		elif next_is_aka:
			akas.append(re.split('AKA: ',line)[1].replace('<span class="delimiter"> | </span>', '|').strip())
			next_is_aka = False
			found_aka = True
		elif line.find('<span class=\"display-name \">') > -1:
			goodies = line.split('<span class=\"display-name \">')[1].split('</span>')[0]
			names.append(goodies.split('>')[1].split('<')[0])
			urls.append(goodies.split('\"')[1] + 'graph?ref_=nm_mtr')
			if (not found_aka):
				akas.append('')
			else:
				found_aka = False
		elif line.find('<span class=\"age_rank sort\">') > -1:
			age = line.split('<span class=\"age_rank sort\">')[1].strip()
			ages.append('' if age == '&nbsp;' else age)
		elif line.find('<span class=\"height sort\">') > -1:
			height = line.split('<span class=\"height sort\">')[1].strip()
			heights.append('' if height == '&nbsp;' else height)
		elif line.find('<li class="job_categories ellipsis">') > -1:
			next_is_role = True
		elif line.find('<li class="known_for ellipsis">') > -1:
			next_is_titles = True
		elif line.find('<li class="aka ellipsis">') > -1:
			next_is_aka = True
		

with open('stars_out.txt','w') as f:
	f.write('rank;name;url;age;height;roles;titles;aliases\n')
	for n in range(1000):
		outline = ';'.join([str(ranks[n]),names[n],urls[n],ages[n],heights[n],roles[n],titles[n],akas[n]]) + '\n'
		outline = outline.replace('&amp;', '&')
		f.write(outline)
			