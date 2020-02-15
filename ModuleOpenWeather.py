"""Current temperature in city"""

import requests


class OpenWheather:
    """
    For temperature in Fahrenheit use units=imperial
    For temperature in Celsius use units=metric
    Temperature in Kelvin is used by default, no need to use units parameter in API call
    """
    def __init__(self, city='Kiev', units='metric', lang='ua'):
        self.api_key = '00d8cfc15e00563c54b8f53919c25083'
        self.api_url = 'http://api.openweathermap.org/data/2.5/weather'

        self.city = city
        self.units = units
        self.lang = lang

        self.params = {
            'q': self.city,
            'appid': self.api_key,
            'units': self.units,
            'lang': self.lang,
        }

        self.res = requests.get(self.api_url, params=self.params)
        self.data = self.res.json()

    def requests(self):
        """
        Q: API calls return an error 401
        A: You can get the error 401 in the following cases:
            - You did not specify your API key in API request.
            - Your API key is not activated yet. Within the next couple of hours, it will be activated and ready to use.
            - You are using wrong API key in API request. Please, check your right API key in personal account.
            - You have FREE subscription and try to get access to our paid services.

        Q: API calls return an error 404
        A:You can get this error in the following cases:
            - You specify wrong city name
            - Check your internet connection

        Q: API calls return an error 429
        A: You will get the error 429 if you have FREE tariff and make more than 60 API calls per minute.
        Please, check your code and reduce the number of calls to our services.

        :return: Response and database
        """
        return self.res, self.data


if __name__ == "__main__":
    OW = OpenWheather()
    print(OW.requests()[0])
    print(OW.requests()[1])

    OW_London_Kelvin_ru = OpenWheather('London', '', 'ru')
    print(OW_London_Kelvin_ru.requests()[0])
    print(OW_London_Kelvin_ru.requests()[1])
