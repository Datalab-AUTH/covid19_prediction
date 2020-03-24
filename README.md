# covid19_prediction
Prediction models for Co-vid 19 usecase. This is a spin-off repository of the main covid19 repository. Here, the data collection, feature engineering and model creation - needed for the prediction task - take place.

## Data sources - Features

1. Daily ECDC data 
    - Per country info - Daily info on cases and deaths
    - Link: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
2. Government Action 
    - Legislature for controlling the spread of the virus
    - Link: https://docs.google.com/spreadsheets/d/1oCieYIoCsKt5ac1aYfR8tWxD4e-y2p2Qz-R1yy39uE8/edit?usp=sharing
3. Geographical Information
    - Bordering Countries and the spread of the virus there
4. Country Indices 
    - Indices about financial state or healthcare of the country, etc.
5. Demographics
    - World Bank
        - % population 0-14 age group: https://data.worldbank.org/
        - % population 15-64 age group: https://data.worldbank.org/
        - % population 64 and above age group: https://data.worldbank.org/
        - total population: https://data.worldbank.org/
        - % population males: https://data.worldbank.org/
        - % population females: https://data.worldbank.org/
        - Current health expenditure (% of GDP): https://data.worldbank.org/
    - OECD
        - Hospital Beds (Latest): https://data.oecd.org/healtheqt/hospital-beds.htm
        - Doctors (Latest): https://data.oecd.org/healthres/doctors.htm
