from fastapi import FastAPI, HTTPException
from models.EloClass import EloClass
from models.Player import Player
from models.Team import Team
from models.IndividualMatch import IndividualMatch
from models.TeamMatch import TeamMatch

app = FastAPI()
elo_system = EloClass()


@app.post("/add_player/", response_description="Player added")
async def add_player(player: Player):
    """
    Add a new player with an initial rating to the Elo system.
    """
    elo_system.add_player(player.player_id)
    return {"message": f"Player {player.player_id} added with rating {elo_system.get_rating(player.player_id)}"}

@app.post("/update_individual_match/", response_description="Ratings updated for individual match")
async def update_individual_match(match: IndividualMatch):
    """
    Update player ratings after an individual match.
    """
    if match.player_a not in elo_system.ratings or match.player_b not in elo_system.ratings:
        raise HTTPException(status_code=404, detail="One or both players not found")
    elo_system.update_individual_ratings(match.player_a, match.player_b, match.score_a)
    return {
        "player_a_rating": elo_system.get_rating(match.player_a),
        "player_b_rating": elo_system.get_rating(match.player_b)
    }

@app.post("/update_team_match/", response_description="Ratings updated for team match")
async def update_team_match(match: TeamMatch):
    """
    Update player ratings after a team match.
    """
    if any(player not in elo_system.ratings for team in [match.team_a, match.team_b] for player in team):
        raise HTTPException(status_code=404, detail="One or more players not found in teams")
    elo_system.update_team_ratings(match.team_a, match.team_b, match.score_a)
    ratings_a = {player: elo_system.get_rating(player) for player in match.team_a}
    ratings_b = {player: elo_system.get_rating(player) for player in match.team_b}
    return {"team_a_ratings": ratings_a, "team_b_ratings": ratings_b}

@app.get("/get_rating/player_id={player_id}", response_description="Retrieve player rating")
async def get_player_rating(player_id: str):
    """
    Retrieve the current rating of a specified player.
    """
    rating = elo_system.get_rating(player_id)
    if rating == "Player not found":
        raise HTTPException(status_code=404, detail="Player not found")
    return {"player_id": player_id, "rating": rating}

@app.post("/get_team_rating/", response_description="Retrieve team rating")
async def get_team_rating(team: Team):
    """
    Retrieve the average rating for a specified team.
    """
    if any(player not in elo_system.ratings for player in team.team):
        raise HTTPException(status_code=404, detail="One or more players not found in team")
    team_rating = elo_system.get_team_rating(team.team)
    return {"team_rating": team_rating}