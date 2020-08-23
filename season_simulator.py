import random

class SeasonSimulator:
    def __init__(self,seasonLen=22):
        # Creating season
        season = {}

        teams1 = [team for team in range(1,10)]
        teams2 = [team for team in range(18,9,-1)]

        for rnd in range(1,seasonLen+1):
            rndList = [(t1,t2) for t1,t2 in zip(teams1,teams2)]
            season.update({rnd : rndList})

            t1 = teams1.pop(-1)
            t2 = teams2.pop(0)

            teams1 = [t2] + teams1
            teams2 = teams2 + [t1]

        # Simulating results
        results = {}
        for rnd in season:
            for teams in season[rnd]:
                try:
                    results[rnd].append(self.GetResult(teams[0],teams[1]))
                except:
                    results.update({rnd : [self.GetResult(teams[0],teams[1])]})

        self.GetRankings(results)

        # for rnd in results:
        #     print(rnd,':')
        #     print(results[rnd])

    @staticmethod
    def GetResult(team1,team2):
        team1Score = int(random.gauss(75,10)) # points
        team2Score = int(random.gauss(75,10)) # points

        if team1Score > team2Score:
            result = 1
        elif team1Score < team2Score:
            result = 0
        else:
            result = .5

        return (team1,team2,team1Score,team2Score,result)

    @staticmethod
    def GetRankings(results):
        seasonTotals = [[i,0,0,0,0,0] for i in range(1,19)]

        for rnd in results:
            for game in results[rnd]:
                seasonTotals[game[0]-1][4] += game[2] # team1 total points for
                seasonTotals[game[0]-1][5] += game[3] # team1 total points against
                seasonTotals[game[1]-1][5] += game[3] # team2 total points for
                seasonTotals[game[1]-1][4] += game[2] # team2 total points against

                if game[4] == 1:
                    seasonTotals[game[0]-1][1] += 1
                    seasonTotals[game[1]-1][2] += 1
                elif game[4] == 0:
                    seasonTotals[game[0]-1][2] += 1
                    seasonTotals[game[1]-1][1] += 1
                elif game[4] == .5:
                    seasonTotals[game[0]-1][3] += 1
                    seasonTotals[game[1]-1][3] += 1

        seasonTotals.sort(key=lambda x: x[5],reverse=False)
        seasonTotals.sort(key=lambda x: x[4],reverse=True)
        seasonTotals.sort(key=lambda x: x[2],reverse=False)
        seasonTotals.sort(key=lambda x: x[1],reverse=True)

        print('Current Ranking System:\n')
        print('[Team,W,L,D,PointsFor,PointsAgainst]:\n')
        for team in seasonTotals:
            print(team)
        print('\n')
                    
    @staticmethod
    def WeightedResult():
        pass
        

SeasonSimulator()
