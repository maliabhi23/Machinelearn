import numpy as np

import pandas as pd
#df=pd.read_csv("data.csv");
#data={
 #   "name":["rakesh","rahul","nitu"],
  #  "age":[45,67,66]
   # };
#df=pd.DataFrame(data);
#Series have one d array means on e column and DataFrame Can Have Multiple Column 
#i=np.array([1,2,3,4,5,6]);
data=[3,4,5,6];
index=[10,11,12,13]

#ser=pd.Series(data,index);
ser=np.array([34,56,66,76,66])
nser=pd.Series(ser)#which is in the form Of The Taulare
#Series is the Nothing But Columns in Table Excel
#column==index
#create series from dict, array,liste
#print(nser); print series from given array

dict1={
    "name":"nitu",
    "age":66
}

#new=pd.Series(np.linspace(3,4,5))
#print(new)
#Creating the Seried From Numpy Function

#Creation of The Series From Range Fun
#ran=pd.Series(range(10))
#print(ran)

#   mathematical function
#ser=np.arange(10,15)
#newSe=pd.Series(data=ser*5,index=ser)
#print(newSe)


#head () return top 5 rows from the table


# reading csv File


new_file=pd.read_csv("nba.csv");
#he=new_file.head()#return First 5 rows 
#print(he);


# to  return 9 rows
n=9;
#newcolum=new_file["Name"]
#top=newcolum.head(n)#print the 9 column
#print(top)

#tail return bootom 5 defau
#ntaile  =new_file.tail()

#series=new_file["Salary"]
#boto=series.tail(n)
#print(boto)

#describe calculate mean,median ,mode 

#print(new_file.describe())
#to remove null values
new_file.dropna(inplace=True)

#Doning on rows and Columns 
data={
    "name":["nital","smitu","ishu"],
    "age":[3,6,66],
}

df=pd.DataFrame(data)

#delete column 
df.drop(["name","age"],axis=1,inplace=True)
#print(df["name"])

#in this adding new fielde
address=["kolhapur","gaganbavde","shirole"]
df["Address"]=address;

print(df)

# work with the excel

newdata=pd.read_csv("nba.csv");