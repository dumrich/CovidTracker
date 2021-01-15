from collections import defaultdict
import csv

class Tracker:
    """covid.ourworldindata.org web scraper to find COVID data"""

    def __init__(self):
        self.data = defaultdict(dict)

    def parse_into_dict(self):
        """Parse the daily covid file into the data dictionary"""
        with open('data.csv') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            for count, row in enumerate(reader):
                if count==0:
                    continue

                elif count==1000:
                    break

                if (country := self.data.get(row[2], None)) is None:
                    self.data[row[2]] = defaultdict(dict)
                    self.data[row[2]].setdefault('New Cases', [])
                self.data[row[2]]["New Cases"].append(row[5])
            return self.data

    def find_country(self, *, country="*"):
        if country=="*":
            return self.data
        else:
            return self.data.get(country, "No data avaliable for this country")


Tracker = Tracker()
Tracker.parse_into_dict()
print(Tracker.find_country(country="Andorra"))
