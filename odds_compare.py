

class odds_compare:

    def __init__(self, api_array):
        self.api_array = api_array

    # calculate odds comparisons for all available matches
    def calculate_comparisons(self):
        result = []

        for i in self.api_array:
            result_dict = {
                "home": "",
                "away": "",
                "home_odds": [],
                "away_odds": []
            }

            result_dict['home'] = i['home_team']
            result_dict['away'] = [x for x in i['teams'] if x != i['home_team']][0]

            home_odds = []
            away_odds = []
            # return all odds
            for book in i['sites']:
                if result_dict['home'] == i['teams'][0]:
                    home_odds.append((book['site_nice'], book['odds']['h2h'][0]))
                    away_odds.append((book['site_nice'], book['odds']['h2h'][1]))
                else:
                    home_odds.append((book['site_nice'], book['odds']['h2h'][1]))
                    away_odds.append((book['site_nice'], book['odds']['h2h'][0]))     

            result_dict['home_odds'] = sorted(home_odds, key=lambda tup: tup[1], reverse=True)
            result_dict['away_odds'] = sorted(away_odds, key=lambda tup: tup[1], reverse=True)

            result.append(result_dict)

        return result

    # calculate odds comparisons for a specific team
    def calculate_comparisons_team(self, team):
        # print(self.api_array)
        result = {
            "home": "",
            "away": "",
            "home_odds": [],
            "away_odds": []
        }

        # look for particular match
        for i in self.api_array:
            if team in i['teams']:
                home_odds = []
                away_odds = []
                # return all odds
                for book in i['sites']:
                    # print(book['site_nice']+ " - " +str(book['odds']['h2h']))
                    home_odds.append((book['site_nice'], book['odds']['h2h'][0]))
                    away_odds.append((book['site_nice'], book['odds']['h2h'][1]))     

                result['home_odds'] = sorted(home_odds, key=lambda tup: tup[1], reverse=True)
                result['away_odds'] = sorted(away_odds, key=lambda tup: tup[1], reverse=True)

                result['home'] = i['home_team']
                result['away'] = [x for x in i['teams'] if x != i['home_team']][0]

                break   # only want first game with selected team from API

        return result

