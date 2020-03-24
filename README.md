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
    - World Bank (Latest data)
        - % population 0-14 age group: https://data.worldbank.org/
        - % population 15-64 age group: https://data.worldbank.org/
        - % population 64 and above age group: https://data.worldbank.org/
        - total population: https://data.worldbank.org/
        - % population males: https://data.worldbank.org/
        - % population females: https://data.worldbank.org/
        - Current health expenditure (% of GDP): https://data.worldbank.org/
    - OECD (Latest data)
        - Hospital Beds: https://data.oecd.org/healtheqt/hospital-beds.htm
        - Doctors per 1000 habitats: https://data.oecd.org/healthres/doctors.htm
        - Nurses per 1000 habitats: https://data.oecd.org/healthres/nurses.htm
        - Daily smokers - Percentage of the population aged 15+: https://data.oecd.org/healthrisk/daily-smokers.htm
        - Overweight or obese population - Percentage of the population aged 15+ (available self-reported data used to fill missing values): https://data.oecd.org/healthrisk/overweight-or-obese-population.htm
        - Alcohol consumption - Annual sales of pure alcohol in litres per person aged 15 years and older: https://data.oecd.org/healthrisk/alcohol-consumption.htm
