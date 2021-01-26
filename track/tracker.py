from collections import defaultdict
import csv
import time
import os


TRACK = ""

if __name__=="__main__":
    TRACK = os.path.abspath(os.path.dirname(__file__))+'/data.csv'
else:
    TRACK=os.path.abspath(os.path.dirname(__file__))+'/data.csv'

class Tracker:
    """covid.ourworldindata.org web scraper to find COVID data"""

    def __init__(self):
        self.data = defaultdict(dict)
        self.date = time.strftime("%Y-%m-%d") 

    def parse_into_dict(self):
        """Parse the daily covid file into the data dictionary"""
        with open(TRACK) as data_file:
            reader = csv.reader(data_file, delimiter=',')
            for count, row in enumerate(reader):
                if count == 0:
                    continue
                
                row[2] = row[2].replace(" ", "").lower()
                if self.data.get(row[2], None) is None:
                    self.data[row[2]] = defaultdict(dict)
                    self.data[row[2]]["region"] = row[0]
                    self.data[row[2]].setdefault('New Cases', [])
                    self.data[row[2]].setdefault('Total Cases', [])
                    self.data[row[2]].setdefault("Total Deaths", [])
                    self.data[row[2]].setdefault("New Deaths", [])
                    self.data[row[2]].setdefault("Cases Per Million", [])
                    self.data[row[2]].setdefault("Total Vaccinations", [])
                    self.data[row[2]].setdefault("Date", [])
                    self.data[row[2]]["Total Population"] = row[40]
                self.data[row[2]]["New Cases"].append(row[5])
                if row[4]=="":
                    temp=0
                else:
                    self.data[row[2]]["Total Cases"].append(row[4])
                self.data[row[2]]["Total Deaths"].append(row[7])
                if row[7]=="":
                    temp=0
                else:
                    self.data[row[2]]["Total Deaths"].append(row[7])
                self.data[row[2]]["New Deaths"].append(row[8])
                self.data[row[2]]["Cases Per Million"].append(row[10])
                self.data[row[2]]["Date"].append(row[3])
                if row[25]=="":
                    temp=0
                else:
                    self.data[row[2]]["Total Tests"] = row[25]
                if row[34]=="":
                    temp = 0 
                else:
                    self.data[row[2]]["Total Vaccinations"] = row[34]
            return self.data

    def find_country(self, *, country="*"):
        country = country.replace(" ", "").lower()
        if country == "*":
            return self.data
        else:
            return self.data.get(country, "No data avaliable for this country")


if __name__ == "__main__":
    Tracker = Tracker()
    Tracker.parse_into_dict()
    print(Tracker.find_country(country="united states")["Total Tests"])
