import pandas as pd

train_test_limit = 32000

types_index = {"Normal":0,"Fire":1,"Water":2,"Electric":3,"Grass":4,"Ice":5,"Fighting":6,"Poison":7,"Ground":8,"Flying":9,"Psychic":10,"Bug":11,"Rock":12,"Ghost":13,"Dragon":14,"Dark":15,"Steel":16,"Fairy":17}
versus_type = pd.read_csv('versus_types.csv')
pokemons = pd.read_csv("pokemon.csv")


pokemons['Legendary'] = pokemons['Legendary'].replace([True,False], [.5,-.5])
pokemons.drop(['Name', 'Type 2', 'Generation'], axis=1, inplace=True)

data_train = {'winner': []}
data_test = {}
data_winners = {'winner': []}

for column in pokemons:
	if column != '#' and column != 'Type 1':
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
	type_ratio = versus_type.iloc[types_index[fp_data['Type 1'].values[0]], types_index[sp_data['Type 1'].values[0]]]
		
	if i < train_test_limit:
		data_train['winner'].append(1 if first_pokemon == winner_pokemon else -1)
	else:
		data_winners['winner'].append(1 if first_pokemon == winner_pokemon else -1)
		
	for column in pokemons:
		if column == 'HP':
			if i < train_test_limit:
				data_train[column].append(fp_data[column].values[0] - sp_data[column].values[0]* .85)
			else:
				data_test[column].append(fp_data[column].values[0] - sp_data[column].values[0]* .85)
		elif column == 'Attack' or column  == 'Sp. Atk':
			if i < train_test_limit:
				data_train[column].append(fp_data[column].values[0]*type_ratio - sp_data[column].values[0])
			else:
				data_test[column].append(fp_data[column].values[0]*type_ratio - sp_data[column].values[0])
		elif column != '#' and column != 'Type 1':
			if i < train_test_limit:
				data_train[column].append(fp_data[column].values[0] - sp_data[column].values[0])
			else:
				data_test[column].append(fp_data[column].values[0] - sp_data[column].values[0])

pd.DataFrame(data_train).to_csv('combats_train.csv', index=False)
pd.DataFrame(data_test).to_csv('combats_test.csv', index=False)
pd.DataFrame(data_winners).to_csv('combats_test_winners.csv', index=False)