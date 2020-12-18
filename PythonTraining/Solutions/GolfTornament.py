'''
Author: Fionn Mcguire
Date: Nov 2020
'''
import random

class GolfTornament(object):
    def __init__(self):
        self.player_ratings = {
            "Sergio Garcia":{"rating":68.99802084636,"stdiv": 2.8022106094,"wins":0,"top_five":0,"simulated_scores":[]},
            "Tiger Woods":{"rating":69.35135041782,"stdiv": 2.7891506279,"wins":0,"top_five":0,"simulated_scores":[]},
            "Kenny Perry":{"rating":69.91471916678,"stdiv": 2.779164583,"wins":0,"top_five":0,"simulated_scores":[]},
            "Gonzalo Fernandez-Castano":{"rating":70.00454323213,"stdiv": 2.80730658184,"wins":0,"top_five":0,"simulated_scores":[]},
            "Rory McIlroy":{"rating":70.03914628487,"stdiv": 2.81525581752,"wins":0,"top_five":0,"simulated_scores":[]},
            "John Cook":{"rating":70.07314839476,"stdiv": 2.748840518,"wins":0,"top_five":0,"simulated_scores":[]},
            "Jaco Van Zyl":{"rating":70.08926215876,"stdiv": 2.78426082931,"wins":0,"top_five":0,"simulated_scores":[]},
            "Brandt Snedeker" :{"rating":70.17987728156,"stdiv": 2.77189131799,"wins":0,"top_five":0,"simulated_scores":[]},
            "Francesco Molinari":{"rating":70.21681358363,"stdiv": 2.74834473201,"wins":0,"top_five":0,"simulated_scores":[]},
            "Matteo Manassero":{"rating":70.22010792006,"stdiv": 2.77346484857,"wins":0,"top_five":0,"simulated_scores":[]},
            "Rocco Mediate":{"rating":70.24975090651,"stdiv": 2.78827651594,"wins":0,"top_five":0,"simulated_scores":[]},
            "Phil Mickelson":{"rating":70.2831986625,"stdiv": 2.77942880401,"wins":0,"top_five":0,"simulated_scores":[]},
            "Justin Rose":{"rating":70.28785317825,"stdiv": 2.75785755538,"wins":0,"top_five":0,"simulated_scores":[]},
            "Jim Furyk":{"rating":70.29979751876,"stdiv": 2.74303206415,"wins":0,"top_five":0,"simulated_scores":[]},
            "Luke Donald":{"rating":70.31075778923,"stdiv": 2.75356932454,"wins":0,"top_five":0,"simulated_scores":[]},
            "South Africa":{"rating":70.32676162032,"stdiv": 2.752106981,"wins":0,"top_five":0,"simulated_scores":[]},
            "Charl Schwartzel":{"rating":70.39461420897,"stdiv": 2.78476477706,"wins":0,"top_five":0,"simulated_scores":[]},
            "Duffy Waldorf":{"rating":70.40624211864,"stdiv": 2.75608325682,"wins":0,"top_five":0,"simulated_scores":[]},
            "Darren Fichardt":{"rating":70.42869494626,"stdiv": 2.7804524764,"wins":0,"top_five":0,"simulated_scores":[]},
            "Jay Haas":{"rating":70.44274917206,"stdiv": 2.712519019,"wins":0,"top_five":0,"simulated_scores":[]}


        }
        self.number_of_simulations = 1000
        self.tournament_rounds = 4

    def import_ratings(self,filepath):
        pass

    def simulate_tournament(self):
        tournament_results = {}
        for key in self.player_ratings:
            for i in range(self.tournament_rounds):
                try:
                    tournament_results[key] += random.normalvariate(self.player_ratings[key]['rating'], self.player_ratings[key]['stdiv'])
                except:
                    tournament_results[key] = random.normalvariate(self.player_ratings[key]['rating'], self.player_ratings[key]['stdiv'])

            self.player_ratings[key]["simulated_scores"].append(tournament_results[key])



    def eval_winner(self):
        for key in self.player_ratings.keys():
            print("%: %".format(key,sum(self.player_ratings[key]["simulated_scores"])/self.number_of_simulations))


    def monte_carlo(self):
        for index in range(self.number_of_simulations):
            self.simulate_tournament()


#Read in the ratings file
#Use this to create the pseudo random numbers
# Use the resulting random numbers to simulate a tournament
#Iterate over the tournament multiple times to get a more accurate guage of the winner.
# Use this results set to determine the winner and top five fractions


new_gf = GolfTornament()
print(new_gf.simulate_tournament())
