import pandas as pd

# Because the data didnt need to be fixed (no na vales) also all the columns seemed relevant none of them needed to be dropped. So we made this file to 
# to show when we could do and to show how a method chaining function could work on the dataset. 

def data_processing(file):
    df = pd.read_csv(file) # reads in the file 
    new = (
        df.drop(df[(df.sex=='female') | (df.age <25) | (df.region != 'southwest')].index) # drops the columns where sex is female, age is less then 25 and where the region is not the southwest
        .sort_values('charges', ascending = False) # sorts the values from highest to lowest based on the charges 
        .rename(columns={'sex' : 'gender', 'children':'kids'}) # renames the sex column to gender and the children column to kids
        .reset_index(drop = True) 
        .loc[:, ["age", "gender", "kids",'smoker','region','charges']]
         )
    return new
