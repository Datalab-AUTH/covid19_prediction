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
4. Country Indices [DONE]
    - Human Freedom indices
        - % On a scale of 0 to 10, where 10 represents more freedom. More info at https://www.cato.org/human-freedom-index-new
    - World happiness report
        - % The following columns: GDP per Capita, Family, Life Expectancy, Freedom, Generosity, Trust Government Corruption describe the extent to which these factors contribute in evaluating the happiness in each country. If you add all these factors up, you get the happiness score so it might be un-reliable to model them to predict Happiness Scores.
5. Demographics
    - World Bank (Latest data) world_bank_data.csv
        - % population 0-14 age group
        - % population 15-64 age group
        - % population 64 and above age group
        - total population
        - % population males
        - % population females
        - Current health expenditure (% of GDP)
    - OECD (Latest data) oecd_data.csv
        - Hospital Beds
        - Doctors per 1000 habitats
        - Nurses per 1000 habitats
        - Daily smokers - Percentage of the population aged 15+
        - Overweight or obese population - Percentage of the population aged 15+ (available self-reported data used to fill missing values)
        - Alcohol consumption - Annual sales of pure alcohol in litres per person aged 15 years and older
