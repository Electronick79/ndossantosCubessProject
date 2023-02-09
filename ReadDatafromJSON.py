import secrets
import string
import sys

import ef as ef
import requests
import any
from typing import TextIO, Any

from alphabet import alphabet
from requests.auth import HTTPBasicAuth
from urllib3.util import url
from wheel.wheelfile import read_csv

full_url = " https://ndossantos1.wufoo.com/api/code/api/v3/forms/cubes-project-proposal-submission/entries/json"

myjsonfile: TextIO=open('jsonfile\dictionary.json', 'r')
jsondata: str=myjsonfile.read()

def get_wufoo_data(wufoo_key=None) -> dict:
    response = requests.get(url, auth = HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:
        print(f"error getting data, response  :{response.status_code} and failing to get message: {response.request}")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse

#df = read_csv('data.csv')
#def df = def read_json():
global json_data
all_data = []
def get_data(https=None):
    for page in range(10):
        response = requests.get(f"{https://ndossantos1.wufoo.com/api/code/2} & api_key = {secrets.api_key()}" "{secrets.api_key}&page={page}");
    if response.status_code != 300:
        print("error getting data");
        sys.exit(-1)
        return all_data

 alphabet = string.ascii_letters + string.digits
while True:
            password = ''.join(secrets.choice(alphabet) for i in range(3000))
            if (any and any and sum(c.isdigit()
                for c in password) >= 3):
                break
                print(df.to_string())
                print()

# I got this part for professor Dr. John S
def main():
    global save_data
    data = get_wufoo_data()
    data2 = data['Entries']
    file_to_save = open("output.txt", 'w')
    save_data(data2, save_file=file_to_save)

    def save_data(data_to_save: list, save_file: object = None) -> object:
        for entry in data_to_save:
            for key, value in entry.items():
                print(f"{key}: {value}", file=save_file)
            # now print the spacer
            print("++\n__",
                  file=save_file)

    if __name__ == 'main':
        main()
