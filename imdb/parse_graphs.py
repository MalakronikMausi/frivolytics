import os, sys

for subdir, dirs, files in os.walk('pro.imdb.com'):

	if not os.path.exists('graphs'):
    		os.makedirs('graphs')
	
	for file in files:

		row1 = ['name']
		row2 = []
		filename = 'oops'

		with open(subdir + '/' + file,'r') as f:
			for line in f:
				if line.find('var pagePathBase') > -1:
					filename = (line.split('var pagePathBase = \'/name/'))[1].split('\'')[0] + '.csv'
				elif line.find(' - IMDbPro</title>') > -1:
					name = (line.split('<title>'))[1].split(' - IMDbPro</title>')[0]
					row2.append(name)
				elif line.find('\"date\" : \"') > -1:
					date = (line.split('\"date\" : \"'))[1].split('T')[0]
					row1.append(date)
				elif line.find('\"rank\" : ') > -1:
					rank = (line.split('\"rank\" : '))[1].split('\n')[0]
					row2.append(rank)

		with open('graphs/' + filename,'w') as f:
			f.write(','.join(row1))
			f.write('\n')
			f.write(','.join(row2))
			f.write('\n')
			