import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier


pokemons = pd.read_csv("pokemon.csv")
pokemons['Legendary'] = pokemons['Legendary'].replace([True,False], [1,-1])
pokemons.drop(['Name'], axis=1, inplace=True)
pokemons = pd.get_dummies(pokemons)


combats = pd.read_csv("combats.csv")
test = pd.read_csv("tests.csv")

data = pd.DataFrame()
winners = pd.DataFrame()

for i in range(0,100):
	data_aux = pd.DataFrame()
	winners_aux = pd.DataFrame()
	
	first_pokemon = combats.iloc[i,0]
	second_pokemon = combats.iloc[i,1]
	winner_pokemon = combats.iloc[i,2]
	fp_data = pokemons[pokemons['#'] == first_pokemon]
	sp_data = pokemons[pokemons['#'] == second_pokemon]

	for column in pokemons:
		if column != '#':
			if i == 0:
				data["P1-"+column] = fp_data[column].values
				data["P2-"+column] = sp_data[column].values
			else:
				data_aux["P1-"+column] = fp_data[column].values
				data_aux["P2-"+column] = sp_data[column].values

	if winner_pokemon == first_pokemon:
		if i == 0:
			winners["Winner"] = [1]
		else:
			winners_aux["Winner"] = [1]
	else:
		if i == 0:
			winners["Winner"] = [-1]
		else:
			winners_aux["Winner"] = [-1]

	if i != 0:
		data = pd.concat([data, data_aux], ignore_index=True)
		winners = pd.concat([winners, winners_aux], ignore_index=True)		


#print data		
pd.concat([data,winners], axis=1).to_csv('result.csv', index=False)

X = data
y = winners

mlp = GradientBoostingClassifier()

#tree = DecisionTreeClassifier(max_depth=3, random_state=0)
mlp.fit(X, y)
print mlp.score(X, y)
