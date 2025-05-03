# main.py
import pandas as pd
from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console

title = "UFO Sightings Dataset"
page_message = "This loads the UFO sightings dataset into a Pandas dataframe and displays the first and last 5 rows."
url = "ufo_sightings.csv"

# set up page text & default URL
pydom["div#page-message"].html = page_message
pydom["input#txt-url"][0].value = url

def log(message):
    console.log(message)

def loadFromURL(event):
    pydom["div#pandas-output-inner"].html = ""
    url = pydom["input#txt-url"][0].value
    log(f"Fetching CSV from {url}")
    df = pd.read_csv(open_url(url))
    # show table & console
    pydom["div#pandas-output"].style["display"] = "block"
    pydom["div#pandas-dev-console"].style["display"] = "block"
    display(df, target="pandas-output-inner", append="False")