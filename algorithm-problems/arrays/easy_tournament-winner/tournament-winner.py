# Notes:
# We can solve this one by iterating the competions array once. In each
# iteration, we map the result to the teams in competition. We keep track
# of the scores and the winning team. When we finished the loop, simply return
# the winning team.
#
# Complexity:
# O(n) time | O(k) space - where n is the number of competitions, and k is the
# number of teams.
HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam: 0}

	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition

		winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

		updateScores(winningTeam, 3, scores)

		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam

	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0

	scores[team] += points
