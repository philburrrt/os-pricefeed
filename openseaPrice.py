import requests
import json
import pprint
import time

with open('./approvedListings.json', 'r') as f:
    approvedListings = json.load(f)

def updateOSPrices(approvedListings):

    priceLog = []

    for entry in approvedListings:
        slug = entry['slug']
        name = entry['assetName']
        url = 'https://api.opensea.io/api/v1/collection/'

        response = requests.get(url + slug)
        data = response.json()

        try:
            floor_price = data['collection']['stats']['floor_price']
            entry['osPrice'] = floor_price
            priceDict = {
                "name": entry['assetName'], 
                "price": floor_price
                }
            priceLog.append(priceDict)
            time.sleep(0.26)
        except:
            print("Error with " + name)
            pass
    
    pprint.pprint(priceLog)
    


def main():
    while True:
        updateOSPrices(approvedListings)
        time.sleep(15)

main()
