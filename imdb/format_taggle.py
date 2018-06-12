import pandas as pd

my_data = pd.read_csv('stars_out.txt', sep=';', header=0)

for n in range(my_data.shape[0]):
	roles = my_data.loc[n]['roles'].split('|')
	for role in roles:
		if not role in my_data.columns:
			my_data.insert(my_data.columns.get_loc('titles') - 1, role, ['0'] * my_data.shape[0])
		my_data.at[n,role] = '1'

my_data.drop('roles', axis=1, inplace=True)

my_data.to_csv('taggle_out.csv', sep=';')
			