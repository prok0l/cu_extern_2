from typing import List

from flask import Blueprint, render_template, current_app, request

from entities.errors.api_error import APIError, APIAuthorizationError, APINumberOfRequests
from entities.forms.location_input import LocationForm
from entities.weather import WeatherInfo
from services.api.backend import Backend

main_bp = Blueprint('main', __name__, template_folder='templates')


@main_bp.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        try:
            form = LocationForm(**request.form)
        except Exception as _:
            return render_template('error.html',
                                   msg='пж не пытайся сломать, отправляя запросы по api')
        api = Backend(api_key=current_app.config['API_KEY'],
                      address=current_app.config['API_URL'])
        try:
            locations = [api.geolocation.get_location_key(location=form.start),
                         api.geolocation.get_location_key(location=form.finish)]

        except ConnectionError:
            return render_template('error.html',
                                   msg='Интернет: кто куда, а я по ...')
        except APIAuthorizationError:
            return render_template('error.html',
                                   msg='Упс, похоже меня неправильно настроили,'
                                       ' попроси админа поправить токен')
        except APINumberOfRequests:
            return render_template('error.html',
                                   msg='Платите доллары $$$ (превышено кол-во запросов)')
        except APIError:
            return render_template('error.html',
                                   msg='Упс, не могу найти такое место',
                                   hidden_msg='Ищите закладку лучше')
        except Exception as _:
            return render_template('error.html',
                                   msg='Где-то в коде ошибка')

        try:
            weather: List[List[WeatherInfo]] = [api.weather.get_weather(location=location) for location in locations]
            return render_template('weather_view.html', weather=weather)

        except APIAuthorizationError:
            return render_template('error.html',
                                   msg='Упс, похоже меня неправильно настроили,'
                                       ' попроси админа поправить токен')
        except APINumberOfRequests:
            return render_template('error.html',
                                   msg='Платите доллары $$$ (превышено кол-во запросов)')
        except APIError:
            return render_template('error.html',
                                   msg='Упс, похоже всевидящий глаз сломался, я не могу\n'
                                       'подсказать тебе погоду')
        except Exception as _:
            return render_template('error.html',
                                   msg='Где-то в коде ошибка')
