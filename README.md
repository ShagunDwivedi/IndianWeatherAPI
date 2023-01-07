## IndianWeatherAPI

The API scrapes the India Meteorological Dept's website to access weather data.

### Function:

- Provides Weather Data based on station's name (duh)
- Returns closest match suggestions if station not present in [city-links](city_links.json).


### Endpoints:

- /station/weather
    - Maximum Temp                  (°C)
    - Minimum Temp                  (°C) 
    - Total Rainfall                (mm) 
    - Relative Humidity at 0830 hrs (%)


- /station/detailed_weather
    - Maximum Temp                  (°C)
    - Departure from Normal         (°C)
    - Minimum Temp                  (°C) 
    - Departure from Normal         (°C)
    - 24 Hours Rainfall             (mm) 
    - Total Rainfall                (mm) 
    - Relative Humidity at 0830 hrs (%)
    - Relative Humidity at 1730 hrs (%) 
    - Todays Sunset                 (IST)	
    - Tomorrow's Sunrise            (IST) 
    - Moonset                       (IST)
    - Moonrise                      (IST) 

- /station/forecast
    - Date	                        (DD-Month)
    - Min Temp	                    (°C)
    - Max Temp	                    (°C)
    - Weather                       (Description)

### To-Do:

- Restructure Folders and remove unnecessary imports/variables
- Delete the ipynb
- ADD A DISCLAIMER (ALL DATA BELONGS TO IMD AND API WILL BREAK WHEN IMD WEBSITE STUCTURE CHANGES) 
- create yaml file
- Schedule updating city-links
