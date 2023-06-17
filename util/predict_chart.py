import pandas as pd
def predict_df(start_date,end_date,selected_features,selected_fan):
    filename = 'pred/'+ selected_fan[:1].zfill(4) + "out.csv"
    df = pd.read_csv(filename)
    start_date=pd.to_datetime(start_date)
    end_date=pd.to_datetime(end_date)
    # 根据选择的特征获取对应列的数据
    selected_columns = []
    selected_features.append('DATATIME')
    # 根据选择的日期范围筛选数据
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    mask = (df['DATATIME'] >= start_date) & (df['DATATIME'] <= end_date)
    df = df.loc[mask]
    df = df[selected_features]
    return df