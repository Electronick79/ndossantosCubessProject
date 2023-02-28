import secrets
import string
import sys
import urllib
import any
import requests
import mysql.connector

from mysql.connector import Error
import pandas as pd

base_url = 'https://ndossantos1.wufoo.com/api/code/2'
username = 'ndossantos1'
password = 'Electronick'

# I got this part from the web page as an example: https://wufoo.github.io/docs/#all-forms

password_manager = urllib.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, base_url, username, password)
handler = urllib.HTTPBasicAuthHandler()
opener = urllib.build_opener(handler)
urllib.install_opener(opener)

response = urllib.urlopen(base_url + 'ndossantos1.wufoo.com/forms/m1jxzvny0fifth1o/fields.json')
data = json.load(response)
print(json.dumps(data, indent=6, sort_keys=True))

from requests.auth import HTTPBasicAuth;
from urllib3.util import url;

full_url = " https://ndossantos1.wufoo.com/api/code/api/v3/forms/cubes-project-proposal-submission/entries/json"


# full_url = "https://ndossantos1.wufoo.com/forms/school-id-registration-form/"

# myjsonfile: TextIO=open('jsonfile\dictionary.json', 'r')
# jsondata: str=jsonfield.read()


#####################################################################################
def get_wufoo_data(wufoo_key=None) -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:
        print(f"error getting data, response  :{response.status_code} and failing to get message: {response.request}")
        sys.exit(-1)
    json_response = response.json()
    return json_response
# df = read_csv('data.csv')
# def df = def read_json():
global json_data
all_data = []

#####################################################################################
res = requests.get('http://{ndossantos1}.wufoo.com/api/v3/forms/{identifier}/fields.{format}')
print(res)
if res:
    print('Response OK')
else:
    print('Response Failed')
    print(res.status_code)
    print(res.headers)

#####################################################################################

# DATA BASE  & SERVER CREATION

# Server Creation
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
        )

        print("MySQL Database connection successful")
    except error as err:
        print(f"Error: '{err}'""")
        return connection
    #put mySQL terminal password
pw =""

# Database name
db = "ndossantos1"
connection = create_server_connection("localhost", roor, pw)

# Create mysql_python
def create_database(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database create successfully")
        except Error as err:
            print(f"Error: '{err}'")
create_database_query = "Create database mysql_phyton"
create_database(connection, create_database_query)

# CONNECTING TO DATA BASE
def create_db_connection(host_name, user_name, user_password, db_name):
    Connection = None
    try:
        connection = mysql.connector.connection(
            host = host_name,
            user = user_name,
            passwd =user_password,
            database = db_name)
        print("MySQL database connection Successfully")
    except Error as err:
        print(f"Error: '{err}""")
    return connection

# Execute sql queries
def execute_query(connection, query):
    cusor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query was successfully")
    except Error as err:
        print(f'Error: '{err}'"")


#####################################################################################
def get_data(https=None):
    for page in range(10):
        response = requests.get(
            f"{https://ndossantos1.wufoo.com/forms/m1jxzvny0ftjh1o/} & api_key = {secrets.api_key()}" "{secrets.api_key}&page={page}");
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


# I got this part from professor Dr. John S

###########################BLOCK#####################################################
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

