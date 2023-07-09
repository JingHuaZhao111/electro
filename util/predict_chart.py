import pandas as pd
from datetime import timedelta
def predict_df(start_date,end_date,selected_features,selected_fan):
    filename = 'pred/'+ selected_fan[:1]+ ".csv"
    df = pd.read_csv(filename)
    # 根据选择的特征获取对应列的数据
    selected_columns = []
    a=selected_features[:]
    a.append('DATATIME')
    # 根据选择的日期范围筛选数据
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    mask = (df['DATATIME'] >= start_date) & (df['DATATIME'] <= end_date)
    df = df.loc[mask]
    df = df[a]
    return df
def real_df(start_date,end_date,selected_features,selected_fan):
    filename = 'data/'+ selected_fan[:1]+ ".csv"
    df = pd.read_csv(filename)
    # 根据选择的特征获取对应列的数据
    selected_columns = []
    a=selected_features[:]
    a.append('DATATIME')
    # 根据选择的日期范围筛选数据
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    mask = (df['DATATIME'] >= start_date) & (df['DATATIME'] <= end_date)
    df = df.loc[mask]
    df = df[a]
    return df