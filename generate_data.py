import pandas as pd

pokemons = pd.read_csv("pokemon.csv")
pokemons['Legendary'] = pokemons['Legendary'].replace([True,False], [.5,-.5])
pokemons.drop(['Name', 'Type 1', 'Type 2', 'Generation'], axis=1, inplace=True)

data_train = {'winner': []}
data_test = {}
data_winners = {'winner': []}

for column in pokemons:
	if column != '#':
		data_test[column] = []
		data_train[column] = []		

combats = pd.read_csv("combats.csv")

# gerando os dados
for i in range(0,50000):
	first_pokemon = combats.iloc[i,0]
	second_pokemon = combats.iloc[i,1]
	winner_pokemon = combats.iloc[i,2]
	fp_data = pokemons[pokemons['#'] == first_pokemon]
	sp_data = pokemons[pokemons['#'] == second_pokemon]
	if i < 30000:
		data_train['winner'].append(1 if first_pokemon == winner_pokemon else -1)
	else:
		data_winners['winner'].append(1 if first_pokemon == winner_pokemon else -1)
		
	for column in pokemons:
		if column != '#':
			if i < 30000:
				data_train[column].append(fp_data[column].values[0] - sp_data[column].values[0])
			else:
				data_test[column].append(fp_data[column].values[0] - sp_data[column].values[0])

pd.DataFrame(data_train).to_csv('combats_train.csv', index=False)
pd.DataFrame(data_test).to_csv('combats_test.csv', index=False)
pd.DataFrame(data_winners).to_csv('combats_test_winners.csv', index=False)