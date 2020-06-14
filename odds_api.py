import json
import requests

class odds_api:


    def api_res(input):

        api_keys = {}
        with open('secret.json', 'r') as f:
            api_keys = json.loads(f.read())

        # api key 
        api_key = api_keys['odds_api'] 

        if input is "NRL":
            sport_key = 'rugbyleague_nrl'
        elif input is "AFL":
            sport_key ='aussierules_afl'

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
