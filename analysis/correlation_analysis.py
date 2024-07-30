# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 16:17:32


import pandas as pd
import matplotlib.pyplot as plt


def correlation_analysis(cleaned_traffic_data_path, cleaned_accident_data_path):
    traffic_data = pd.read_csv(cleaned_traffic_data_path)
    accident_data = pd.read_csv(cleaned_accident_data_path)

    traffic_data['mes_ano'] = pd.to_datetime(
        traffic_data['mes_ano'], format='%d/%m/%Y')
    monthly_traffic_volume = traffic_data.groupby(
        traffic_data['mes_ano'].dt.to_period('M'))['volume_total'].sum()

    accident_data['data_inversa'] = pd.to_datetime(
        accident_data['data_inversa'])
    monthly_accidents = accident_data.groupby(
        accident_data['data_inversa'].dt.to_period('M')).size()

    traffic_accidents_df = pd.DataFrame({
        'Volume_Trafego': monthly_traffic_volume,
        'Numero_Acidentes': monthly_accidents
    })

    correlation = traffic_accidents_df.corr()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Mês')
    ax1.set_ylabel('Volume de Tráfego', color=color)
    ax1.plot(traffic_accidents_df.index.astype(
        str), traffic_accidents_df['Volume_Trafego'], color=color, marker='o', label='Volume de Tráfego')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Número de Acidentes', color=color)
    ax2.plot(traffic_accidents_df.index.astype(
        str), traffic_accidents_df['Numero_Acidentes'], color=color, marker='o', label='Número de Acidentes')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')

    plt.title('Volume de Tráfego e Número de Acidentes em MG (2020)')
    plt.grid(True)
    fig.tight_layout()
    plt.show()

    print('Correlação:', correlation)
