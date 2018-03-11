import os
DAO_PATH=os.path.abspath(__file__)
BASE_PATH=os.path.dirname(os.path.dirname(DAO_PATH))
MAIN_PATH=os.path.join(BASE_PATH, 'main')


DATA_PATH=os.path.join(BASE_PATH, 'data')
DATA_WEATHERDATA_PATH=os.path.join(DATA_PATH, 'historical-hourly-weather-data')