import unittest
from src.weather_fetcher import get_weather

class TestWeatheretcher(unittest.TestCase):
    def test_get_weather(self):
        #calling the fn
        temp,description=get_weather()
        #basic checks
        self.assertIsInstance(temp,(int,float),"Temperature")
        self.assertIsInstance(description,str,"Weather Description")

if __name__=='__main__':
    unittest.main()