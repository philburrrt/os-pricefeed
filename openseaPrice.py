import requests
import json
import time
import pandas as pd


with open('./approvedListings.json', 'r') as f:
    approvedListings = json.load(f)

    

def updateOSPrices(approvedListings):

    priceLog = []

    for entry in approvedListings:
        slug = entry['slug']
        name = entry['assetName']
        
        url = 'https://api.opensea.io/api/v1/collection/'

        try:
            response = requests.get(url + slug)
            data = response.json()

            floor_price = data['collection']['stats']['floor_price']
            entry['osPrice'] = floor_price
            priceDict = {
                "name": name, 
                "price": floor_price
                }
            priceLog.append(priceDict)
            time.sleep(0.26)
        except:
            print('Error with ' + slug)
            continue


    feed = pd.DataFrame(priceLog)
    print(feed)
    


def main():
    while True:
        updateOSPrices(approvedListings)
        time.sleep(15)

main()
