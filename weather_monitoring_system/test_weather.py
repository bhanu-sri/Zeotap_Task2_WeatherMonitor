import unittest
from api_client import get_weather_data
from data_processing import kelvin_to_celsius

class TestWeatherApp(unittest.TestCase):
    
    def test_kelvin_to_celsius(self):
        self.assertEqual(round(kelvin_to_celsius(300), 2), 26.85)
    
    def test_weather_api(self):
        data = get_weather_data('Delhi')
        self.assertIn('main', data)

if __name__ == '__main__':
    unittest.main()
