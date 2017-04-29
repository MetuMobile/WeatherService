
class Weather:
    def __init__(self):
        pass

    def getDaily(self):
        import json
        from urllib.request import urlopen
        url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20u=%27c%27%20and%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22kapouti%2C%20cy%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

        response = urlopen(url)
        response = response.read()

        jsonEndpointData = json.loads(response)
        """ refactoring idea in python3 for the lines 11,12,13:
        with urlopen(url) as res:
            jsonEndpointData = json.loads(res.read().decode())
        """
        currentAndForecastWeather = {}
        currentAndForecastWeather['units'] = jsonEndpointData['query']['results']['channel']['units']
        currentAndForecastWeather['current'] = jsonEndpointData['query']['results']['channel']['item']['condition']
        currentAndForecastWeather['today'] = jsonEndpointData['query']['results']['channel']['item']['forecast'][0]
        currentAndForecastWeather['tomorrow'] = jsonEndpointData['query']['results']['channel']['item']['forecast'][1]

        currentAndForecastWeather['current']['imageUrl'] = self.getImageLink(currentAndForecastWeather['current']['code'])
        currentAndForecastWeather['today']['imageUrl'] = self.getImageLink(currentAndForecastWeather['today']['code'])
        currentAndForecastWeather['tomorrow']['imageUrl'] = self.getImageLink(currentAndForecastWeather['tomorrow']['code'])

        return currentAndForecastWeather

    def getImageLink(self, code):
        code = int(code)
        if code in range(0,5): 
            return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        elif code in range(5, 10):
            return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        elif code in range(10, 13):
            return 'http://l.yimg.com/a/i/us/we/52/12.gif'
        elif code in range(13, 17) or code == 46:
            return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        elif code in (17,19):
            return 'http://l.yimg.com/a/i/us/we/52/17.gif'
        elif code in range(19, 31):
            return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        elif code in (31, 33):
            return 'http://l.yimg.com/a/i/us/we/52/31.gif'
        elif code in range(32,37,2): 
            return 'http://l.yimg.com/a/i/us/we/52/32.gif'
        elif code == 35: 
            return 'http://l.yimg.com/a/i/us/we/52/35.gif'
        elif code in (37,38): 
            return 'http://l.yimg.com/a/i/us/we/52/37.gif'
        elif code in (39,40):
            return 'http://l.yimg.com/a/i/us/we/52/39.gif'
        elif code in range(41, 44):
            return 'http://l.yimg.com/a/i/us/we/52/41.gif'
        elif code in (42, 43): 
            return 'http://l.yimg.com/a/i/us/we/52/41.gif'
        elif code == 44:
            return 'http://l.yimg.com/a/i/us/we/52/44.gif'
        elif code in (45, 47): 
            return 'http://l.yimg.com/a/i/us/we/52/45.gif'
        return 'http://l.yimg.com/a/i/us/we/52/3200.gif'
