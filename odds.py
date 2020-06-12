from odds_compare import odds_compare
from odds_api import odds_api


class Odds():

    def __init__(self, input):
        self.input = input


    def get_odds(self):

        # based on number send in correct team
        # team = 'Canterbury Bulldogs'

        odds_json =odds_api.api_res(self.input)
        odds_json = odds_json['data']

        new_odds_compare = odds_compare(odds_json)
        result = new_odds_compare.calculate_comparisons()

        result_final = self.beautify_output(result)

        return result_final


    def beautify_output(self, game_list_input):
        
        final_string = ""
        for game in game_list_input:
            final_string += f"{game['home']} vs {game['away']}\n\n"
            final_string += f"{game['home']}:\n"
            for book in game['home_odds']:
                final_string += str(book).replace('(', '').replace(')', '').replace('\'', '').replace(',', ':')
                final_string += "\n"

            final_string += f"\n{game['away']}:\n"

            for book in game['away_odds']:
                final_string += str(book).replace('(', '').replace(')', '').replace('\'', '').replace(',', ':')
                final_string += "\n"
            final_string += "********\n\n"

        return final_string