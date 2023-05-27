
# imports
import requests


def get_units():
    # asks user for choice of units
    while True:
        units = input('What units would you like to use? Enter \'F\' for Fahrenheit, \'C\' for Celsius, \'K\' for Kelvin: ')
        if units.upper() == 'F':
            return 'imperial'
        elif units.upper() == 'C':
            return 'metric'
        elif units.upper() == 'K':
            return 'standard'
        else:
            print('Unit not recognized.')


def get_json(city_or_zip, units, api_key):
    # returns the json data for a specified city or zip code
    if city_or_zip.isnumeric():  # zip codes
        try:
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units={}'.format(city_or_zip, 'US', api_key, units))
        except requests.exceptions.RequestException:  # catch-all for connection errors
            return 'Connection Error'
        r_data = r.json()
        return r_data
    else:  # city/state
        state_code = input('Input the two-letter state abbreviation: ')
        try:
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}&units={}'.format(city_or_zip, state_code, 'US', api_key, units))
        except requests.exceptions.RequestException:
            return 'Connection Error'
        r_data = r.json()
        return r_data


def pretty_print(data, units):
    # prints the data nicely for the user to see
    name = data['name']
    if units == 'imperial':
        temp_unit = 'F'
    elif units == 'metric':
        temp_unit = 'C'
    elif units == 'standard':
        temp_unit = 'K'
    else:  # as written, this else condition should never be reached
        return
    main_data = data['main']
    clouds = data['clouds']
    print()  # adds space between the input line and the printed info
    print('Weather for {}:'.format(name))
    print('---------------------------------------------------------')
    print('{:<20} {}\N{DEGREE SIGN} {}'.format('Current Temperature:', main_data['temp'], temp_unit))
    print('{:<20} {}\N{DEGREE SIGN} {}'.format('Feels Like:', main_data['feels_like'], temp_unit))
    print('{:<20} {}\N{DEGREE SIGN} {}'.format('High Temperature:', main_data['temp_max'], temp_unit))
    print('{:<20} {}\N{DEGREE SIGN} {}'.format('Low Temperature:', main_data['temp_min'], temp_unit))
    print('{:<20} {} hPa'.format('Pressure:', main_data['pressure']))
    print('{:<20} {}%'.format('Humidity:', main_data['humidity']))
    print('{:<20} {}%'.format('Cloud Coverage:', clouds['all']))  # I actually prefer this to 'partly cloudy', etc.
    print()  # separating the block of weather info from the rest


def run_again():
    # asks user if they want to run the program again and returns boolean True or False based on response
    while True:
        again = input('Would you like to do another lookup? Type \'yes\' or \'no\': ')
        if again.lower() == 'yes':
            return True
        elif again.lower() == 'no':
            return False
        else:
            print('Not recognized.')


def main():
    api_key = '9a4c223835d827a254119da4a4eb94c5'
    run = True
    print('Welcome to the Weather Looker Upper!')
    units = get_units()  # it feels natural to set units before searching for weather data...just a personal choice
    while run:
        city_or_zip = input('Please enter the city name or zip code, or write \'units\' to change units: ')
        if city_or_zip.lower() == 'units':  # pretty sure there is no city called 'units' in the US...
            units = get_units()
            continue
        city_data = get_json(city_or_zip, units, api_key)
        if city_data == 'Connection Error':  # in case there is a connection error
            print('Connection unsuccessful. Please check connection and try again.')
            continue
        try:  # checks if the city is found
            main_data = city_data['main']
            clouds = city_data['clouds']
        except KeyError:  # city not found
            print('Location not recognized. Please try again.')
            continue
        pretty_print(city_data, units)
        run = run_again()  # run the program again?
        if run:
            units = get_units()
        else:
            print('Bye!')


if __name__ == '__main__':
    main()
