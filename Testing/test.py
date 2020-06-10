# from itertools import chain


# def beautify_output(game_list_input):

#     final_string = ""
#     for game in game_list_input:
#         final_string += f"{game['home']} vs {game['away']}\n\n"
#         final_string += f"{game['home']}:\n"
#         for book in game['home_odds']:
#             final_string += str(book).replace('(', '').replace(')', '').replace('\'', '').replace(',', ':')
#             final_string += "\n"

#         final_string += f"\n{game['away']}:\n"

#         for book in game['away_odds']:
#             final_string += str(book).replace('(', '').replace(')', '').replace('\'', '').replace(',', ':')
#             final_string += "\n"
#         final_string += "********\n\n"

#     return final_string



# game_list = [{'home': 'Manly Warringah Sea Eagles', 'away': 'Brisbane Broncos', 'home_odds': [('Betfair', 4.7), ('Bet Easy', 4.55), ('TAB', 4.5), ('Neds', 4.5), ('SportsBet', 4.35), ('Unibet', 4.3)], 'away_odds': [('Betfair', 1.24), ('Unibet', 1.22), ('Bet Easy', 1.21), ('SportsBet', 1.21), ('TAB', 1.2), ('Neds', 1.2)]}, {'home': 'New Zealand Warriors', 'away': 'North Queensland Cowboys', 'home_odds': [('TAB', 2.9), ('Betfair', 2.88), ('Unibet', 2.8), ('SportsBet', 2.79), ('Bet Easy', 2.75), ('Neds', 2.75)], 'away_odds': [('Betfair', 1.49), ('Unibet', 1.45), ('Bet Easy', 1.45), ('Neds', 1.45), ('SportsBet', 1.45), ('TAB', 1.42)]}, {'home': 'Parramatta Eels', 'away': 'Penrith Panthers', 'home_odds': [('Betfair', 1.48), ('Unibet', 1.45), ('Bet Easy', 1.45), ('Neds', 1.45), ('SportsBet', 1.45), ('TAB', 1.44)], 'away_odds': [('Betfair', 2.82), ('Unibet', 2.8), ('TAB', 2.8), ('Bet Easy', 2.8), ('SportsBet', 2.78), ('Neds', 2.75)]}, {'home': 'South Sydney Rabbitohs', 'away': 'Gold Coast Titans', 'home_odds': [('Unibet', 4.2), ('TAB', 4.2), ('Bet Easy', 4.2), ('SportsBet', 4.2), ('Betfair', 4.1), ('Neds', 3.9)], 'away_odds': [('Neds', 1.25), ('Unibet', 1.24), ('TAB', 1.23), ('Betfair', 1.23), ('SportsBet', 1.23), ('Bet Easy', 1.22)]}, {'home': 'Newcastle Knights', 'away': 'Melbourne Storm', 'home_odds': [('Neds', 1.65), ('Bet Easy', 1.63), ('TAB', 1.6), ('Betfair', 1.59), ('Unibet', 1.58), ('SportsBet', 1.58)], 'away_odds': [('TAB', 2.4), ('SportsBet', 2.39), ('Unibet', 2.38), ('Betfair', 2.32), ('Bet Easy', 2.3), ('Neds', 2.25)]}, {'home': 'Wests Tigers', 'away': 'Canberra Raiders', 'home_odds': [('TAB', 1.37), ('Betfair', 1.37), ('Neds', 1.36), ('Unibet', 1.35), ('Bet Easy', 1.33), ('SportsBet', 1.33)], 'away_odds': [('Bet Easy', 3.3), ('SportsBet', 3.3), ('Unibet', 3.25), ('TAB', 3.1), ('Neds', 3.1), ('Betfair', 2.9)]}, {'home': 'Canterbury Bulldogs', 'away': 'Sydney Roosters', 'home_odds': [('SportsBet', 8.0), ('TAB', 7.5), ('Bet Easy', 7.5), ('Neds', 7.0), ('Unibet', 6.5), ('Betfair', 5.4)], 'away_odds': [('Betfair', 1.13), ('Unibet', 1.12), ('Neds', 1.1), ('TAB', 1.09), ('Bet Easy', 1.09), ('SportsBet', 1.08)]}, {'home': 'St George Illawarra Dragons', 'away': 'Cronulla Sutherland Sharks', 'home_odds': [('Unibet', 1.44), ('Betfair', 1.41), ('SportsBet', 1.41), ('TAB', 1.4), ('Bet Easy', 1.4), ('Neds', 1.38)], 'away_odds': [('TAB', 3.0), ('Bet Easy', 3.0), ('Neds', 3.0), ('SportsBet', 2.93), ('Unibet', 2.85), ('Betfair', 2.8)]}]


# print(beautify_output(game_list))


    
