# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-07-30 15:20:35
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-07-30 15:27:39


import pandas as pd
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def preprocess_data(traffic_data_path, accident_data_path, cleaned_traffic_data_path, cleaned_accident_data_path):
    # Load and clean traffic data
    traffic_data = pd.read_csv(
        traffic_data_path, delimiter=';', encoding='latin1', quotechar='"')
    traffic_data.columns = [remove_accents(
        col) for col in traffic_data.columns]
    for col in traffic_data.select_dtypes(include=['object']).columns:
        traffic_data[col] = traffic_data[col].apply(
            lambda x: remove_accents(x) if isinstance(x, str) else x)
    traffic_data.to_csv(cleaned_traffic_data_path,
                        index=False, encoding='utf-8')

    # Load and clean accident data
    accident_data = pd.read_csv(
        accident_data_path, delimiter=';', encoding='latin1', quotechar='"')
    accident_data.columns = [remove_accents(
        col) for col in accident_data.columns]
    for col in accident_data.select_dtypes(include=['object']).columns:
        accident_data[col] = accident_data[col].apply(
            lambda x: remove_accents(x) if isinstance(x, str) else x)
    accident_data.to_csv(cleaned_accident_data_path,
                         index=False, encoding='utf-8')
