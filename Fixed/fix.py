import pandas as pd
import os

cirs = []

paths = [x for x in os.listdir() if '.csv' in x]

dfs = [pd.read_csv(path) for path in paths]

for df in dfs:
	cirs.append(list(df['CIR']))

intersec = []
for sub in cirs:
	for x in sub:
		ok = True
		for sub2 in cirs:
			if x not in sub2:
				ok = False
				break
		if ok: intersec.append(x)
cirs = sorted(list(set(intersec)))

cirs = [str(x) for x in cirs]

for i in range(len(dfs)):
	df = dfs[i]
	df = df[df['CIR'].isin(cirs)]
	df.to_csv('Fixed/' + paths[i], index = False)

with open('Fixed/cirlist.csv', 'w') as f:
	f.write('CIR\n')
	f.write('\n'.join([str(x) for x in cirs]))
