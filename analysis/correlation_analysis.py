# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 15:28:27


import pandas as pd
import matplotlib.pyplot as plt


def correlation_analysis(cleaned_traffic_data_path, cleaned_accident_data_path):
    traffic_data = pd.read_csv(cleaned_traffic_data_path)
    accident_data = pd.read_csv(cleaned_accident_data_path)

    traffic_data['mes_ano'] = pd.to_datetime(
        traffic_data['mes_ano'], format='%d/%m/%Y')
    monthly_traffic_volume = traffic_data.groupby(
        traffic_data['mes_ano'].dt.to_period('M')).sum()['volume_total']

    accident_data['data_inversa'] = pd.to_datetime(
        accident_data['data_inversa'])
    monthly_accidents = accident_data.groupby(
        accident_data['data_inversa'].dt.to_period('M')).size()

    traffic_accidents_df = pd.DataFrame({
        'Volume_Trafego': monthly_traffic_volume,
        'Numero_Acidentes': monthly_accidents
    })

    correlation = traffic_accidents_df.corr()

    plt.figure(figsize=(12, 6))
    traffic_accidents_df['Volume_Trafego'].plot(
        kind='line', marker='o', color='blue', label='Volume de Tráfego')
    plt.title('Volume de Tráfego e Número de Acidentes em MG (2020)')
    plt.ylabel('Volume de Tráfego')
    plt.grid(True)
    plt.legend()

    plt.twinx()
    traffic_accidents_df['Numero_Acidentes'].plot(
        kind='line', marker='o', color='red', label='Número de Acidentes')
    plt.ylabel('Número de Acidentes')
    plt.grid(True)
    plt.legend()

    plt.show()

    print('Correlação:', correlation)
