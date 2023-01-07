## IndianWeatherAPI

Scrapes the Indian Meteorological Dept's website to access weather data.

### Function:

Returns closest match suggestions if station not present in [city-links](city_links.json).

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

