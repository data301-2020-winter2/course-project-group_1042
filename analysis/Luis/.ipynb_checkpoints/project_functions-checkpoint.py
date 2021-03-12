import pandas as pd

def data_processing_rename(file):
    df = pd.read_csv(file)
    df2 = df.rename(columns = {'age':'Age', 'sex':'Sex', 'bmi':'BMI', 'children':'Children', 'smoker':'Smoker', 'region':'Region', 'charges':'Medical Costs'})
    return df2

def data_processing_age_sort(file):
    df = data_processing_rename(file)
    df2 = (
        df.sort_values('Age', ascending = True) #sorts the data by age
        .reset_index(drop = True) #resets the index
    )
    return df2

def data_processing_sex_sort(file):
    df = data_processing_rename(file)
    df2 = (
        df.sort_values('Sex', ascending = True) #sorts the data by region
        .reset_index(drop = True) #resets the index
    )
    return df2

def data_processing_region_sort(file):
    df = data_processing_rename(file)
    df2 = (
        df.sort_values('Region', ascending = True) #sorts the data by region
        .reset_index(drop = True) #resets the index
    )
    return df2

def data_processing_children_sort(file):
    df = data_processing_rename(file)
    df2 = (
        df.sort_values('Children', ascending = True) #sorts the data by region
        .reset_index(drop = True) #resets the index
    )
    return df2

def data_processing_smoker_sort(file):
    df = data_processing_rename(file)
    df2 = (
        df.sort_values('Smoker', ascending = True) #sorts the data by region
        .reset_index(drop = True) #resets the index
    )
    return df2