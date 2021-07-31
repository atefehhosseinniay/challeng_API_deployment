import pandas as pd
import numpy as np
import json
import joblib


def cleaning_data():
    # import dataset scraped from immoweb during our previous challenge
    ds = pd.read_csv(r'C:\Users\atefe\Desktop\challenge_api\data\data_admin.csv', index_col=[0])

    # dropping rows without price or area
    ds.dropna(subset=['price', 'area'], inplace=True)

    # Keeping only first row for rows having same city, price, room_number and area
    ds.drop_duplicates(['location', 'type', 'subtype', 'price', 'room_number', 'area'], keep='first', inplace=True,
                       ignore_index=True)

    # prices between 80k€ and 2M€
    ds = ds[(80000 <= ds.price) & (ds.price <= 2e6)]

    # no grouped properties
    ds = ds[~ds['subtype'].isin(['MIXED_USE_BUILDING', 'APARTMENT_BLOCK'])]

    # bedrooms <15
    ds = ds[ds.room_number < 15]

    # Convert missing values with median score for terrace_area and garden_area, and facade_count.if we have terrace and garden we convert missing values to median if not we convert it to 0

    # terrace_area
    ds.loc[ds.terrace == 1, 'terrace_area'] = ds.loc[ds.terrace == 1, 'terrace_area'].fillna(
        ds['terrace_area'].median())
    ds.loc[ds.terrace == 0, 'terrace_area'] = ds.loc[ds.terrace == 0, 'terrace_area'].fillna(0.0)

    # garden_area
    ds.loc[ds.garden == 1, 'garden_area'] = ds.loc[ds.garden == 1, 'garden_area'].fillna(ds['garden_area'].median())
    ds.loc[ds.garden == 0, 'garden_area'] = ds.loc[ds.garden == 0, 'garden_area'].fillna(0.0)

    # facade_count

    ds['facade_count'] = ds['facade_count'].fillna(ds['facade_count'].median())

    # dropping rows with missing values for building_condition
    ds.dropna(subset=['building_condition'], inplace=True)

    # convert missing values with 0.0 for land_surface. all missing values corresponds to the APARTMENT.

    ds['land_surface'] = ds['land_surface'].fillna(0.0)

    # Create dummy variables for categirical data

    type_num = pd.get_dummies(ds['type'], drop_first=False)
    building_condition_num = pd.get_dummies(ds['building_condition'], drop_first=False)
    region_num = pd.get_dummies(ds['Region'], drop_first=False)
    province_num = pd.get_dummies(ds['Province'], drop_first=False)
    # subtype_num = pd.get_dummies(ds['subtype'], drop_first=False)

    ds = pd.concat([ds, type_num, building_condition_num, region_num, province_num], axis=1)

    # convert type of dummy columns to int
    ds.iloc[:, 22:] = ds.iloc[:, 22:].astype(np.int64)

    # convert float64 to int64
    ds["area"] = ds["area"].astype(np.int64)
    ds["terrace_area"] = ds["terrace_area"].astype(np.int64)
    ds["garden_area"] = ds["garden_area"].astype(np.int64)
    ds["land_surface"] = ds["land_surface"].astype(np.int64)
    ds["facade_count"] = ds["facade_count"].astype(np.int64)

    # drop subtype. we don't use this columns in our model.
    ds.drop('subtype', axis=1, inplace=True)

    return ds


def preprocess(data):
    model_columns = joblib.load(r'C:\Users\atefe\Desktop\challenge_api\model\model_columns.pkl')
    type_num = pd.get_dummies(data['type'], drop_first=False)
    building_condition_num = pd.get_dummies(data['building_condition'], drop_first=False)
    province_num = pd.get_dummies(data['Province'], drop_first=False)
    region_num = pd.get_dummies(data['Region'], drop_first=False)


    data = pd.concat([data, type_num, building_condition_num, region_num, province_num], axis=1)
    data = data.reindex(columns=model_columns, fill_value=0)
    return data

#df=cleaning_data()
#print(df.columns)
#model_columns = joblib.load(r'C:\Users\atefe\Desktop\challenge_api\model\model_columns.pkl')
#print(model_columns)




#df = pd.DataFrame(json_)
#data = preprocess(df)
#print(data.columns)
#print(data.info())
#print(data.columns)
#print(data.info)