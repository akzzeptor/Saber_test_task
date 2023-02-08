import requests
import csv
import json
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import datetime

# Импорт списка активов (помимо названия активов содержится также дополнительная мнформация)
url = "http://api.coincap.io/v2/assets"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
json_data = json.loads(response.text.encode("utf8"))
coin_list = json_data["data"]
coin_data = pd.DataFrame(coin_list)
#Создание selectbox  для выбора актива
asset_symbol = st.sidebar.selectbox("Select an asset", coin_data.symbol)

select_assets = coin_data.loc[coin_data["symbol"] == asset_symbol, "id"].iloc[0]
#Импорт истории измениений цены выбранного активова во времени
url1 = "http://api.coincap.io/v2/assets/{0:s}/history?interval=d1".format(select_assets)
payload1 = {}
headers1 = {}
response1 = requests.request("GET", url1, headers=headers1, data=payload1)
json_data1 = json.loads(response1.text.encode("utf8"))
asset = json_data1["data"]
df_coin_history = pd.DataFrame(asset)
df_coin_history["datetime"] = pd.to_datetime(df_coin_history["time"], unit="ms")
df_coin_history["priceUsd"] = pd.to_numeric(df_coin_history["priceUsd"])
#Определение минимальных и максимальных значений дат в df
min_time = pd.to_datetime(df_coin_history.datetime.min())
max_time = pd.to_datetime(df_coin_history.datetime.max())
#Создание коробок ввода дат для изменения границ оси х (времени) барчарта
start = st.sidebar.date_input("Date from", min_time)
finish = st.sidebar.date_input("Date to", max_time)

df_coin1 = df_coin_history[
    (df_coin_history["datetime"] >= pd.to_datetime(start))
    & (df_coin_history["datetime"] <= pd.to_datetime(finish))
]
#Создание барчарта
df_coin_chart = st.bar_chart(
    data=df_coin1,
    x="datetime",
    y="priceUsd",
    width=0,
    height=0,
    use_container_width=True,
)
