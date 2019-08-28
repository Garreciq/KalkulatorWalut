import requests
from flask import Flask

kalk = Flask(__name__)

@kalk.route("/")
def main():
    return "First Page"

url = "http://api.nbp.pl/api/exchangerates/tables/C/today/?format=json"

r = requests.get(url)
print(r)

if __name__ == "__main__":
    kalk.run()