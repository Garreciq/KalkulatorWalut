import requests
from flask import Flask, render_template

kalk = Flask(__name__)

@kalk.route("/")
def main():
    return render_template('index.html')

url = "http://api.nbp.pl/api/exchangerates/tables/C/today/?format=json"

r = requests.get(url)
print(r)

if __name__ == "__main__":
    kalk.run()