import requests
import json
import pprint
import time

with open('./approvedListings.json', 'r') as f:
    approvedListings = json.load(f)

def updateOSPrices(approvedListings):

    while True:

        for entry in approvedListings:
            slug = entry['slug']
            name = entry['assetName']
            url = 'https://api.opensea.io/api/v1/collection/'

            response = requests.get(url + slug)
            data = response.json()

            try:
                floor_price = data['collection']['stats']['floor_price']
                entry['osPrice'] = floor_price
                pprint.pprint({
                    "name": entry['assetName'], 
                    "price": floor_price
                    })
                time.sleep(2)
            except:
                print("Error with " + name + " slug")
                pass

updateOSPrices(approvedListings)