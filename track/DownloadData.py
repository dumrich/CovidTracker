import os
import subprocess

print("Beginning COVID File download... \n")

URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
if os.path.exists("data.csv"):
    os.remove("data.csv")

if __name__ == "__main__":
    print("Downloading...")
    data = subprocess.run(["curl", URL, ">", "data.csv"], capture_output=True)
    print("Done.")
