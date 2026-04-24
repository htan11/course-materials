##colab file:
##https://colab.research.google.com/drive/1HPOwsi-AMsPwf49ElIZptOfiGYAvpuwn?usp=sharing

import random
import pandas as pd

data=[]

for i in range(1000):
    n=random.randint(5,100)
    r=random.uniform(1,100)
    d=random.uniform(1,50)
    l=random.uniform(0,0.3)
    t=random.uniform(5,50)

    th=r*(1-l)*(n/100)
    la=d*(1+l)

    data.append([n,r,d,l,t,th,la])

df=pd.DataFrame(data,columns=["n","r","d","l","t","th","la"])
df

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error,r2_score

x=df[["n","r","d","l","t"]]
y=df["th"]

x1,x2,y1,y2=train_test_split(x,y,test_size=0.2)

models={
"lr":LinearRegression(),
"dt":DecisionTreeRegressor(),
"rf":RandomForestRegressor(),
"svm":SVR(),
"knn":KNeighborsRegressor()
}

res=[]

for name,m in models.items():
    m.fit(x1,y1)
    p=m.predict(x2)
    mse=mean_squared_error(y2,p)
    r2=r2_score(y2,p)
    res.append([name,mse,r2])

res
