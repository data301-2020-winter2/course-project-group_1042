import pandas as pd

def data_processing(file):
    df = pd.read_csv(file)
    new = (
        df.drop(df[(df.sex=='female') | (df.age <25) | (df.region != 'southwest')].index)
        .sort_values('charges', ascending = False)
        .rename(columns={'sex' : 'gender', 'children':'kids'})
        .reset_index(drop = True)
        .loc[:, ["age", "gender", "kids",'smoker','region','charges']]
         )
    return new
