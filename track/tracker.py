from collections import defaultdict
import csv
import time
import os

class Tracker:
    """covid.ourworldindata.org web scraper to find COVID data"""

    def __init__(self):
        self.data = defaultdict(dict)
        self.date = time.strftime("%Y-%m-%d") 

    def parse_into_dict(self):
        """Parse the daily covid file into the data dictionary"""
        with open(os.path.abspath(os.getcwd())+'/track/data.csv') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            for count, row in enumerate(reader):
                if count == 0:
                    continue

                if self.data.get(row[2], None) is None:
                    self.data[row[2]] = defaultdict(dict)
                    self.data[row[2]].setdefault('New Cases', [])
                    self.data[row[2]].setdefault('Total Cases', [])
                    self.data[row[2]].setdefault("Total Deaths", [])
                    self.data[row[2]].setdefault("New Deaths", [])
                    self.data[row[2]].setdefault("Cases Per Million", [])
                    self.data[row[2]]["Start Date"] = row[3]
                self.data[row[2]]["New Cases"].append(row[5])
                self.data[row[2]]["Total Cases"].append(row[4])
                self.data[row[2]]["Total Deaths"].append(row[7])
                self.data[row[2]]["New Deaths"].append(row[8])
                self.data[row[2]]["Cases Per Million"].append(row[10])
            return self.data

    def find_country(self, *, country="*"):
        if country == "*":
            return self.data
        else:
            return self.data.get(country, "No data avaliable for this country")


if __name__ == "__main__":
    Tracker = Tracker()
    Tracker.parse_into_dict()
    print(Tracker.find_country(country="United States")["Cases Per Million"])
