import pandas as pd

cirs = []
anos = []

paths = [
	'2006-2015_NumeroEstabelecimentosSaudePublicos',
	'2006-2015_NumEstabelecimentosSaudePrivados',
	'2006-2017_NumLeitosObstetricos_ExistenteVsEsperado',
	'2006-2018_EquipamentosBercoAquecidoIncubadora',
	'2006-2018_EstabelecimentosAcompanhamentoPreNatalRisco',
	'2006-2018_NumeroUBS',
	'2006-2018_NumeroUbsPor10kHabitantes',
	'2007-2018_CoberturaEstimadaPopulacaoResidentePorEquipesSaude',
	'RegSaude_TxMortNeonatal'
]

dfs = [pd.read_csv(path + '.csv') for path in paths]

for df in dfs:
	cirs.append(list(df['CIR']))
	anos.append([int(x.split('_')[0]) for x in list(df.columns) if x != 'CIR'])

intersec = []
for sub in anos:
	for x in sub:
		ok = True
		for sub2 in anos:
			if x not in sub2:
				ok = False
				break
		if ok: intersec.append(x)
anos = sorted(list(set(intersec)))

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

anos = [str(x) for x in anos]
cirs = [str(x) for x in cirs]

for i in range(len(dfs)):
	df = dfs[i]
	if i != 2:
		df = df[['CIR'] + anos]
	else:
		df = df.drop(['2006_EX', '2006_ES', '2011_EX', '2011_ES', '2016_EX', '2016_ES', '2017_EX', '2017_ES'], axis = 1)
	df = df[df['CIR'].isin(cirs)]
	df.to_csv('Fixed/' + paths[i] + '.csv', index = False)

print('Anos:', ', '.join(anos))