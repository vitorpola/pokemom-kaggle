import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('combats_train.csv')
test = pd.read_csv('combats_test.csv')
test_winners = pd.read_csv('combats_test_winners.csv')

winners = train['winner']
train = train.drop('winner', axis = 1)

mlp = RandomForestClassifier()
mlp.fit(train, winners)
predict_winners = mlp.predict(test)

correct_count = 0

for i in range(0,len(test_winners)):
	if test_winners.iloc[i,0] == predict_winners[i]:
		correct_count += 1
print (correct_count*1.0)/(len(test_winners))