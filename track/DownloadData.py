import wget
import os

print("Beginning COVID File download... \n")

URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
wget.download(URL, os.path.abspath(os.getcwd())+'/data.csv')
