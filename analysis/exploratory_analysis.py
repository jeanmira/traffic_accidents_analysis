# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 16:15:56


import pandas as pd
import matplotlib.pyplot as plt


def exploratory_analysis(cleaned_traffic_data_path, cleaned_accident_data_path):
    traffic_data = pd.read_csv(cleaned_traffic_data_path)
    accident_data = pd.read_csv(cleaned_accident_data_path)

    traffic_data['mes_ano'] = pd.to_datetime(
        traffic_data['mes_ano'], format='%d/%m/%Y')
    monthly_traffic_volume = traffic_data.groupby(
        traffic_data['mes_ano'].dt.to_period('M'))['volume_total'].sum()

    plt.figure(figsize=(12, 6))
    monthly_traffic_volume.plot(
        kind='line', marker='o', label='Volume de Tráfego')
    plt.title('Volume de Tráfego nas Praças de Pedágio em MG (2020)')
    plt.xlabel('Mês')
    plt.ylabel('Volume Total de Veículos')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    accident_data['data_inversa'] = pd.to_datetime(
        accident_data['data_inversa'])
    monthly_accidents = accident_data.groupby(
        accident_data['data_inversa'].dt.to_period('M')).size()

    plt.figure(figsize=(12, 6))
    monthly_accidents.plot(kind='bar', color='skyblue',
                           edgecolor='black', label='Número de Acidentes')
    plt.title('Número de Acidentes em MG (2020)')
    plt.xlabel('Mês')
    plt.ylabel('Número de Acidentes')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    weekday_accidents = accident_data['dia_semana'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    weekday_accidents.plot(kind='bar', color='lightgreen',
                           edgecolor='black', label='Número de Acidentes')
    plt.title('Número de Acidentes por Dia da Semana em MG (2020)')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Número de Acidentes')
    plt.legend(loc='best')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    causes_accidents = accident_data['causa_acidente'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    causes_accidents.plot(kind='bar', color='salmon',
                          edgecolor='black', label='Número de Acidentes')
    plt.title('Principais Causas de Acidentes em MG (2020)')
    plt.xlabel('Causa do Acidente')
    plt.ylabel('Número de Acidentes')
    plt.legend(loc='best')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    severity_accidents = accident_data[[
        'feridos_leves', 'feridos_graves', 'ilesos', 'mortos']].sum()

    plt.figure(figsize=(12, 6))
    severity_accidents.plot(kind='bar', color='lightcoral',
                            edgecolor='black', label='Número de Pessoas')
    plt.title('Severidade dos Acidentes em MG (2020)')
    plt.xlabel('Tipo de Severidade')
    plt.ylabel('Número de Pessoas')
    plt.legend(loc='best')
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.show()
