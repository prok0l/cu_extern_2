import datetime

from config import load_config, Config
from entities.coords import LocationName
from entities.location import Location
from entities.weather import WeatherInfo, DayPart
from services.api.backend import Backend

if __name__ == '__main__':
    conf: Config = load_config()
    back = Backend(api_key=conf.api_key, address=conf.api_url)
    print(back.geolocation.get_key_by_location(LocationName(name='Tokio')))
    # weathers = back.weather.get_weather(location=Location(name='Moscow', key='1602770'))
    # print(weathers)
    weather = WeatherInfo(day=datetime.datetime.now(),
                          day_part=DayPart.DAY,
                          location=Location(coords=(13, 15), name='Moscow', key='1242413'),
                          wind_speed=10,
                          humidity=50,
                          rain_p=40,
                          temp=20)
    weather.make_msg()
    print(weather.msg)
