import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('mymoviedb.csv',lineterminator='\n')
print(df.head())     # it gives the first 5 rows

df.info()     # to see if there is any null value in dataset or not

print(df['Genre'].head())

print(df.duplicated().sum())   # check if is any duplicate value is +nt in dataset or not , if not then sum will be 0.

print(df.describe())    # it gives the stats of dataset like cnt,mean,std,min,25% etc...


# convert time from string(object) to datetime format 
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)

# remove date and month from date column,we need only year
df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtypes) 

print(df.head())

# dropping the column
cols=['Overview','Original_Language','Poster_Url']
df.drop(cols,axis=1,inplace=True)     # inplace is used for permanent
print(df.columns)
print(df.head())

# Categorize the Vote_avg col and make 4 diff categories popular,avg,below_avg,not_popular to describe it more using categorize_col function

def categorize_col(df,col,labels):
    edges=[df[col].describe()['min'],
           df[col].describe()['25%'],
           df[col].describe()['50%'],
           df[col].describe()['75%'],
           df[col].describe()['max']]
    
    df[col]=pd.cut(df[col],edges,labels=labels,duplicates='drop')    # cut is used for categorization
    return df

labels = ['not_popular','below_avg','average','popular']

categorize_col(df,'Vote_Average',labels)
print(df['Vote_Average'].unique())

print(df.head())


# to check how many movies are pop,avg,below_avg and not_popular
print(df['Vote_Average'].value_counts())

df.dropna(inplace=True)
print(df.isna().sum())

# split genres into a list and then explode the dataframe to have only one genre per row for each movie

df['Genre']=df['Genre'].str.split(', ')    # remove commas and whitespace from genre
df=df.explode('Genre').reset_index(drop=True)
print(df.head())

# casting col into category

df['Genre']=df['Genre'].astype('category')
print(df['Genre'].dtypes)

print(df.info())             #give info about data
print(df.nunique())
print(df.head())

# Data visualization
sns.set_style('whitegrid')
     # most frequent genre of movies released on netflix
df['Genre'].describe()
sns.catplot(y='Genre',data=df,kind='count',
            order=df['Genre'].value_counts().index,
            color='#4287f5')   # color code is for blue color
plt.title('Genre Column Distribution')
plt.show()

    # highest vote in vote_avg col 
sns.catplot(y='Vote_Average',data=df,kind='count',
            order=df['Vote_Average'].value_counts().index,
            color='#4287f5')
plt.title("Votes Distribution")
plt.show()

    # which movie got the highest popularity and what is its genre
print(df[df['Popularity']==df['Popularity'].max()])

    # which movie got the highest popularity and what is its genre
print(df[df['Popularity']==df['Popularity'].min()])

    # which year has the most filmmed movies
df['Release_Date'].hist()
plt.title('Release_Date Column Distribution')
plt.show()










