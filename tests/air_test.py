import urllib.request

# check if air data returns 200
def test():
    url = "https://www.visualcrossing.com/weather/weather-data-services"
    status_code = urllib.request.urlopen(url).getcode()
    assert status_code == 200