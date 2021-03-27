import pandas as pd

# Because the data didnt need to be fixed (no na vales) also all the columns seemed relevant none of them needed to be dropped. So we made this file to 
# to show when we could do and to show how a method chaining function could work on the dataset. 

def data_processing(file):
    df = pd.read_csv(file) # read in the csv file and converts it to the dataframe
    df['smoker'] = df['smoker'].map({'yes':True ,'no':False})
    df['region'] = df['region'].map({'southwest':'sw' ,'northwest':'nw', 'southeast': 'se', 'northeast' : 'ne'})
    new = (
        df.sort_values('charges', ascending = False) # sorts the dataset on the charges column 
        
        .rename(columns={'sex' : 'Sex', 'children':'Children', 'bmi' : 'BMI', 'smoker' : 'Smoker', 'age' : 'Age', 'region' : 'Region', 'charges' : 'Charges'}) #Capitalizes each column in the dataframe
        .reset_index(drop = True)
        # resets the index and then drops the newly made column 
    )
    return new 
        
#df['commissioned'] = df['commissioned'].map({'yes':True ,'no':False})