import pandas as pd
import random
import datetime

id = []
scores = []
limeScores = []

print("Generating dataset")
for i in range(10000):
	if i % 100 == 0:
			print("Iteration: %d" %i)
	id.append(i)
	scores.append(random.random())
	limeScores.append(random.random())

df = pd.DataFrame({
	'scores':scores,
	'limeScores':limeScores
	}, index=id)
df.index.name='id'

df.to_csv("data.csv")
