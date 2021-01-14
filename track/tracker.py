from collections import defaultdict
import wget

URL = 'https://www.worldometers.info/coronavirus/country/us/'

class Tracker:
    """ourworldindata.org web scraper to find COVID data"""

    URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv" 

    def __init__(self, country="*"):
        self.country = country
        self.data = defaultdict([])

    @classmethod
    def GetAllData(cls):
        "Get total world data from ourworldindata"
        wget.download(cls.URL, '/WorldData.xlsx')
