import numpy as np


def myfunction( x ):
	return sum(x)


my_data = genfromtxt('stars_out.txt', delimiter=';', names=True)


all_roles = {}

for n in my_data.shape[0]:
	roles = my_data[n]['roles'].split('|')
	print roles
	for role in roles:
		if not role in all_roles:
			all_roles[role] = [False] * my_data.shape[0])
		all_roles[role][n] = True

for role in all_roles:
	numpy.insert(my_data, all_roles[role], axis=1)






	with open('graphs/' + filename,'w') as f:
		f.write(','.join(row1))
		f.write('\n')
		f.write(','.join(row2))
		f.write('\n')
			