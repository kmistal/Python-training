import requests
import json
from key_store import app_id
from weather_report import WeatherReport


def start():
    print_header()
    get_weather_info()


def print_header():
    print('---------------------')
    print('     WEATHER APP     ')
    print('---------------------')


def get_zip_code():
    return input('Type in zip code: ')


def get_weather_info():
    zip_code = get_zip_code()

    if is_valid_zip_code(zip_code):
        try:
            weather_report = fetch_weather_by_zip_code(zip_code)
            print_weather(weather_report)
        except Exception as error:
            print(error)
    else:
        print('Invalid zip code')


def is_valid_zip_code(zip_code):
    return zip_code.isnumeric() and len(zip_code) == 5 and int(zip_code) > 9999


def fetch_weather_by_zip_code(zip_code):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={}'.format(
        zip_code) + ',us&units=metric&appid={}'.format(app_id)
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return WeatherReport(
            description=weather_data['weather'][0]['description'],
            temperature=weather_data['main']['temp'],
            city=weather_data['name'])
    elif response.status_code == 404:
        raise Exception('City not found for given zip code')
    else:
        raise Exception(
            'Make sure you\'ve provided correct zip code and you have an internet connection.')


def print_weather(weather_report: WeatherReport):
    print('In {} there\'s a {} and the temperature is {} deegres Celcius'.format(weather_report.city,
                                                                                 weather_report.description.lower(),
                                                                                 weather_report.temperature))


if __name__ == "__main__":
    start()
