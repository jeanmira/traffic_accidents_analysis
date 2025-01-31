
# Traffic Accidents Analysis

This project performs a comprehensive analysis of traffic accidents in Minas Gerais (MG), Brazil, using data from toll plazas and reported traffic incidents. The goal is to identify trends, correlations, and hotspots of traffic accidents to provide insights for improving road safety.

## Project Structure

```
├── LICENSE
├── README.md
├── analysis
│   ├── __init__.py
│   ├── correlation_analysis.py
│   ├── data_preprocessing.py
│   ├── exploratory_analysis.py
│   └── hotspot_analysis.py
├── data
│   ├── datatran2020.csv
│   ├── processed
│   │   ├── datatran2020-cleaned.csv
│   │   └── volume-trafego-praca-pedagio-2020-cleaned.csv
│   └── volume-trafego-praca-pedagio-2020.csv
├── main.py
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jeanmira/traffic_accidents_analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd traffic_accidents_analysis
   ```

3. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to preprocess data, perform exploratory analysis, correlation analysis, and hotspot analysis:
   ```bash
   python3 main.py
   ```

## Scripts

- `data_preprocessing.py`: Preprocesses the raw data by cleaning and formatting it.
- `exploratory_analysis.py`: Performs exploratory data analysis, including visualizations of traffic volume and accident trends.
- `correlation_analysis.py`: Analyzes the correlation between traffic volume and the number of accidents.
- `hotspot_analysis.py`: Identifies hotspots of traffic accidents using spatial analysis.

## Data

- `volume-trafego-praca-pedagio-2020.csv`: Contains traffic volume data from toll plazas in 2020.
- `datatran2020.csv`: Contains reported traffic incident data in 2020.

### Data Sources

- [PRF Open Data](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)
- [ANTT Open Data](https://dados.antt.gov.br/dataset/volume-trafego-praca-pedagio)

## Results

The results of the analysis include:
- Trends in traffic volume and accidents over time.
- Correlation between traffic volume and the number of accidents.
- Identification of accident hotspots.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact [Jean Mira](https://github.com/jeanmira).

## Acknowledgements

This project was developed with the help of data provided by public authorities and open data initiatives.
