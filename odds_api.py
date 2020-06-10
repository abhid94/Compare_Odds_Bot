import json
import requests

class odds_api:

    @staticmethod
    def api_res():

        api_keys = {}
        with open('secret.json', 'r') as f:
            api_keys = json.loads(f.read())

        # api key 
        api_key = api_keys['odds_api'] 
        sport_key = 'rugbyleague_nrl'

        odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
            'api_key': api_key,
            'sport': sport_key,
            'region': 'au', # uk | us | eu | au
            'mkt': 'h2h' # h2h | spreads | totals
        }) 

        odds_json = json.loads(odds_response.text)
        if not odds_json['success']:
            print(
                'There was a problem with the odds request:',
                odds_json['msg']
            )

        else:
            # Check your usage
            print('Remaining requests', odds_response.headers['x-requests-remaining'])
            print('Used requests', odds_response.headers['x-requests-used'])

        return odds_json
