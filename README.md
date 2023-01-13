# IndianWeatherAPI

Flask-Restful API that scrapes the India Meteorological Dept's website to access weather data.

## Functions:

- Access brief or detailed weather report based on station's name.
- Get forecast for the next seven days.
- Returns closest match suggestions if station not present in [city-links](./utils/city_links.json).
    - Run [city_links.py](./utils/city_links.py) to update the list.

## Setup:

- Install ```python``` and ```pip```
- Install all dependencies by running:
```python
pip install -r requirements.txt
```
- Run the app:
```python
python3 main.py
```

## API Documentation

To view the documentation refer to [this](api.yaml) document.

## Disclaimer

- All data belongs to India Meteorological Department, the API only accesses and provides content published on [IMD Website](https://city.imd.gov.in/citywx/localwx.php) without modification. The project is NOT affiliated to IMD in any way.
- The tool may crash as soon as the structure of the website changes.

