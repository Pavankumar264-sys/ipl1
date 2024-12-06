from utils.db import db


class Matches(db.Model):
    match_id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100),  nullable=False)
    date = db.Column(db.String(50), nullable=False)
    team1= db.Column(db.String(50), nullable=False)
    team2 = db.Column(db.String(50), nullable=False)
    toss_winner= db.Column(db.String(50), nullable=False)
    toss_decision= db.Column(db.String(50), nullable=False)
    match_winner = db.Column(db.String(40), nullable=False)
    win_by_runs = db.Column(db.String(50), nullable=False)
    win_by_wickets = db.Column(db.String(50), nullable=False)
    player_of_match = db.Column(db.String(50), nullable=False)
    venue = db.Column(db.String(50), nullable=False)
    umpire1 = db.Column(db.String(50), nullable=False)
    umpire2 = db.Column(db.String(50), nullable=False)




class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name=db.Column(db.String(50), nullable=False)


class IPLPlayer(db.Model):  # Specify the table name for IPL players

    # Defining the columns for the table
    player_id = db.Column(db.Integer, primary_key=True)  # Unique ID for each player
    player_name = db.Column(db.String(255), nullable=False)  # Name of the player
    team = db.Column(db.String(255), nullable=False)  # Name of the team
    matches_played = db.Column(db.Integer, nullable=False)  # Total matches played by the player
    runs_scored = db.Column(db.Integer, nullable=False)  # Total runs scored by the player
    wickets_taken = db.Column(db.Integer, nullable=False)  # Total wickets taken


    


