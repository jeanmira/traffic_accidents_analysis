# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 15:26:37


import os
from analysis.data_preprocessing import preprocess_data
from analysis.exploratory_analysis import exploratory_analysis
from analysis.correlation_analysis import correlation_analysis
from analysis.hotspot_analysis import hotspot_analysis


def main():
    # Paths to raw data
    traffic_data_path = 'data/volume-trafego-praca-pedagio-2020.csv'
    accident_data_path = 'data/datatran2020.csv'

    # Paths to cleaned data
    cleaned_traffic_data_path = 'data/processed/volume-trafego-praca-pedagio-2020-cleaned.csv'
    cleaned_accident_data_path = 'data/processed/datatran2020-cleaned.csv'

    # Preprocess data
    preprocess_data(traffic_data_path, accident_data_path,
                    cleaned_traffic_data_path, cleaned_accident_data_path)

    # Perform exploratory analysis
    exploratory_analysis(cleaned_traffic_data_path, cleaned_accident_data_path)

    # Perform correlation analysis
    correlation_analysis(cleaned_traffic_data_path, cleaned_accident_data_path)

    # Perform hotspot analysis
    hotspot_analysis(cleaned_accident_data_path)


if __name__ == "__main__":
    main()
