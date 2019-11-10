import pandas as pd

files = [
	'2006-2015_NumeroEstabelecimentosSaudePublicos.csv',
	'2006-2015_NumEstabelecimentosSaudePrivados.csv',
	'2006-2017_NumLeitosObstetricos_ExistenteVsEsperado.csv',
	'2006-2018_NumeroUBS.csv',
	'2006-2018_NumeroUbsPor10kHabitantes.csv',
	'2007-2018_CoberturaEstimadaPopulacaoResidentePorEquipesSaude.csv',
	'RegSaude_TxMortNeonatal.csv'
]

values = []

def intersect(a, b):
	return [x for x in a if x in b]

for file in files:
	df = pd.read_csv(file)
	vals = df['CIR'].apply(str).unique().tolist()
	values.append(vals)
	del(df)

cirs = values[0]

for i in range(1, len(values)):
	cirs = intersect(cirs, values[i])

with open('cirs.txt', 'w') as f:
	f.write(','.join([str(k) for k in cirs]))