# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 15:28:37


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def hotspot_analysis(cleaned_accident_data_path):
    accident_data = pd.read_csv(cleaned_accident_data_path)

    accident_data['latitude'] = accident_data['latitude'].str.replace(
        ',', '.').astype(float)
    accident_data['longitude'] = accident_data['longitude'].str.replace(
        ',', '.').astype(float)

    latitudes = accident_data['latitude'].values
    longitudes = accident_data['longitude'].values

    xmin, xmax = latitudes.min(), latitudes.max()
    ymin, ymax = longitudes.min(), longitudes.max()
    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack([latitudes, longitudes])

    kernel = stats.gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)

    plt.figure(figsize=(12, 6))
    plt.imshow(np.rot90(Z), cmap='hot', extent=[ymin, ymax, xmin, xmax])
    plt.scatter(longitudes, latitudes, c='blue', s=1, label='Acidentes')
    plt.colorbar(label='Densidade de Acidentes')
    plt.title('Densidade de Acidentes em Minas Gerais')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
