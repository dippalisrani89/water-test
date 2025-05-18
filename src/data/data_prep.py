import pandas as pd
import numpy as np
import os

#train_data = pd.read_csv("./data/raw/train.csv")
#test_data = pd.read_csv("./data/raw/test.csv")
def load_data(filepath: str)-> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from from {filepath}:{e}")

def fill_missing_with_median(df):
    try:
        for column in df.columns:
            if df[column].isnull().any():
                median_value = df[column].median()
                df[column].fillna(median_value,inplace=True)
        return df
    except Exception as e:
        raise Exception(f"Error filling Missing Values:{e}")
        

#train_processed_data  = fill_missing_with_median(train_data)
#test_processed_data  = fill_missing_with_median(test_data)

def save_data(df : pd.DataFrame, filepath:str)->None:
    try:
        df.to_csv(filepath,index=False)
    except Exception as e:
        raise Exception(f"Error saving data to {filepath}:{e}")

#data_path = os.path.join("data","processed")
#os.makedirs(data_path)

#train_processed_data.to_csv(os.path.join(data_path,"train_processed.csv"),index=False)
#test_processed_data.to_csv(os.path.join(data_path,"test_processed.csv"),index=False)

def main():
    try:
        raw_data_path = "./data/raw/"
        processed_data_path = "./data/processed/"
        train_data=load_data(os.path.join(raw_data_path,"train.csv"))
        test_data=load_data(os.path.join(raw_data_path,"test.csv"))
        train_processed_data = fill_missing_with_median(train_data)
        test_processed_data = fill_missing_with_median(test_data)
        os.makedirs(processed_data_path)
        save_data(train_processed_data,os.path.join(processed_data_path,"train_processed.csv"))
        save_data(test_processed_data,os.path.join(processed_data_path,"test_processed.csv"))
    except Exception as e:
        raise Exception(f"An error Occured:{e}")

if __name__ == "__main__":
    main()
