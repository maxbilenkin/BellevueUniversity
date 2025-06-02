#DSC510-T303 Introduction to Programming (2251-1)
#Week 12
#12.1 Programming Assignment Week 12
#Author Maxim Bilenkin
#11/09/2024

import requests

#Change#:1
#Change(s) Made: Created Weather program.
#Date of Change: 11/10/2024
#Author: Maxim Bilenkin
#Change Approved by: Maxim Bilenkin
#Date Moved to Production: 11/16/2024

# URLs for OpenWeather API.
url_api = {
    'lat_and_lon': 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}',
    'city_and_state': 'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={API_key}',
    'zip_code': 'https://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={API_key}'
}

api_key ="685a27e8d3ae37f288db402b5d7debf8"

# Method to get user option.
def get_user_option():
    while True:
            print('Please choose a search option to get weather:')
            print('1: Zip Code')
            print('2: City and State')
            user_option = input('Enter number of your choice: \n')
            if user_option in ['1', '2']:
                return user_option
            else:
                print('Incorrect option. Please enter "1" or "2".')

# Method to get user measurement option.
def get_user_temperature_measurement_unit():
        while True:
            print('Please enter temperature unit:')
            print('1 for Celsius')
            print('2 for Fahrenheit')
            unit_measurement = input('Enter number of your option: \n')
            if unit_measurement in ['1', '2']:
                return unit_measurement
            else:
                print('Invalid unit option. Please enter "1" or "2".')

# Method to get user request based on option.
def get_user_request(user_option):
    if user_option == '1':
        while True:
            zip_code = input('Enter zip code: \n')
            if zip_code.isdigit():
                return {'zip_code': zip_code, 'country_code': 'US', 'API_key': api_key}
            else:
                print('Invalid zip code. Please enter correct numeric value for zip code.')
    elif user_option == '2':
        while True:
            city = input('Enter city: \n')
            if all(x.isalpha() or x.isspace() for x in city):
                break
            else:
                print('Invalid city. Please enter correct city name.')

        while True:
            state = input('Enter state: \n')
            if len(state) == 2 and all(x.isalpha() or x.isspace() for x in state):
                return {'city_name': city.title(), 'state_code': state.title(), 'country_code': 'US', 'API_key': api_key}
            else:
                print('Invalid state. Please enter correct state.')

def get_weather(api, params):
    try:
        response = requests.get(api.format(**params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

# Method to extract, convert and print out all weather details.
def display_weather_details(weather_details, unit_option, city=None, state=None):
    main = weather_details.get('main',{})
    weather = weather_details.get('weather', [{}])[0]
    wind = weather_details.get('wind', {})
    clouds = weather_details.get('clouds',{})
    country = weather_details.get('sys', {}).get('country', '')

    if city and state:
        location = f'{city}, {state}, {country}'
    else:
        location = weather_details.get('name') + ', ' + country

    temp_k = main.get('temp')
    feels_like_k = main.get('feels_like')
    temp_min = main.get('temp_min')
    temp_max = main.get('temp_max')
    pressure = main.get('pressure')
    humidity = main.get('humidity')
    weather_description = weather.get('description')
    wind_speed = wind.get('speed')
    cloudiness = clouds.get('all')

    if unit_option == '1':
        temperature = temp_k - 273.15
        feels_like = feels_like_k - 273.15
        temp_min = temp_min - 273.15
        temp_max = temp_max - 273.15
        temp_unit = '°C'
    elif unit_option == '2':
        temperature = (temp_k - 273.15) * 9/5 + 32
        feels_like = (feels_like_k - 273.15) * 9/5 +32
        temp_min = (temp_min - 273.15) * 9/5 + 32
        temp_max = (temp_max - 273.15) * 9/5 + 32
        temp_unit = '°F'
    else:
        print('Invalid unit option. Routing to Celsius.')
        temperature = temp_k - 273.15
        feels_like = feels_like_k - 273.15
        temp_min = temp_min - 273.15
        temp_max = temp_max - 273.15
        temp_unit = '°C'

    print(f'\nThe Weather in {location.title()} as follows:')
    print(f'-'*42)
    print(f'Temperature: {temperature:.2f}{temp_unit}')
    print(f'Feels Like: {feels_like:.2f}{temp_unit}')
    print(f'Low temp: {temp_min:.2f}{temp_unit}')
    print(f'High temp:{temp_max:.2f}{temp_unit}')
    print(f'Pressure: {pressure} hPa')
    print(f'Humidity: {humidity}%')
    print(f'Weather: {weather_description}')
    print(f'Wind Speed: {wind_speed} m/s')
    print(f'Cloudiness: {cloudiness}%')

def main():
    while True:
        option = get_user_option()
        unit_option = get_user_temperature_measurement_unit()

        while True:
            user_response = get_user_request(option)
            if user_response:
                if option == '1':
                    api = url_api['zip_code']
                elif option == '2':
                    api = url_api['city_and_state']
                    city = user_response['city_name']
                    state = user_response['state_code']

                geographic_response = get_weather(api, user_response)

                if geographic_response:
                    if option == '1':
                        lat = geographic_response['lat']
                        lon = geographic_response['lon']
                        params = {'lat': lat, 'lon': lon, 'API_key': api_key}
                        weather_api = url_api['lat_and_lon']
                        weather_response = get_weather(weather_api, params)
                        state_response = get_weather(url_api['city_and_state'],
                                                     {'city_name': geographic_response['name'], 'state_code': '',
                                                      'country_code': 'US', 'API_key': api_key})
                        state = state_response[0]['state'] if state_response and 'state' in state_response[0] else 'N/A'
                        display_weather_details(weather_response, unit_option, geographic_response['name'], state)


                    else:
                        lat = geographic_response[0]['lat']
                        lon = geographic_response[0]['lon']
                        params = {'lat': lat, 'lon': lon, 'API_key': api_key}
                        weather_api = url_api['lat_and_lon']
                        weather_response = get_weather(weather_api, params)
                        display_weather_details(weather_response, unit_option, city, state)
                else:
                    print('Please enter correct city or state name.\n')
                    continue

            while True:
                another_search = input('Would you like to search weather for another location? Enter "Yes" or "No":\n').strip().lower()
                if another_search == 'yes':
                    break
                elif another_search == 'no':
                    print('Thank you and have a nice day!')
                    return
                else:
                    print('Invalid entry. Please enter "Yes" or "No"')

if __name__=="__main__":
    main()