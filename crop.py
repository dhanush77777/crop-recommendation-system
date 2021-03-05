import pandas as pd
import pickle
df=pd.read_csv(r'C:\Users\SAIDHANUSH\Crop_recommendation.csv')

x=df.iloc[:,[0,1,2,3,4,5,6]]
y=df.iloc[:,[7]]

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(x,y)
pickle.dump(rf,open('crop.pkl','wb'))
p=df['label'].unique()