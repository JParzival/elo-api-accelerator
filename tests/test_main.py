from fastapi.testclient import TestClient
import sys
sys.path.append('R:/Desktop/elo-api-accelerator/app/')  # Adjust the path to include where main.py is located
from main import app

client = TestClient(app)

INITIAL_RATING = 1500

def test_add_player():
    # Test adding a player successfully
    response = client.post("/add_player/", json={"player_id": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Player Alice added with rating 1500"}

    # Test adding a badly formed player
    response = client.post("/add_player/", json={"player_id": 1})
    assert response.status_code == 422 

def test_get_player_rating():
    # Ensure the player exists before testing
    client.post("/add_player/", json={"player_id": "Bob"})
    response = client.get("/get_rating/player_id=Bob")
    assert response.status_code == 200
    assert response.json() == {"player_id": "Bob", "rating": INITIAL_RATING}

    # Test for a non-existing player
    response = client.get("/get_rating/player_id=Charlie")
    assert response.status_code == 404

def test_update_individual_match():
    # Add players first
    client.post("/add_player/", json={"player_id": "Alice"})
    client.post("/add_player/", json={"player_id": "Bob"})
    response = client.post("/update_individual_match/", json={
        "player_a": "Alice",
        "player_b": "Bob",
        "score_a": 1
    })
    assert response.status_code == 200
    results = response.json()
    assert results["player_a_rating"] > INITIAL_RATING
    assert results["player_b_rating"] < INITIAL_RATING

def test_update_team_match():
    # Add players and update team match
    client.post("/add_player/", json={"player_id": "Alice"})
    client.post("/add_player/", json={"player_id": "Bob"})
    client.post("/add_player/", json={"player_id": "Charlie"})
    client.post("/add_player/", json={"player_id": "Dave"})
    response = client.post("/update_team_match/", json={
        "team_a": ["Alice", "Bob"],
        "team_b": ["Charlie", "Dave"],
        "score_a": 1
    })
    assert response.status_code == 200
    ratings = response.json()
    assert ratings["team_a_ratings"]["Alice"] > INITIAL_RATING
    assert ratings["team_a_ratings"]["Bob"] > INITIAL_RATING
    assert ratings["team_b_ratings"]["Charlie"] < INITIAL_RATING
    assert ratings["team_b_ratings"]["Dave"] < INITIAL_RATING

def test_get_team_rating():
    # Add players and retrieve team rating
    client.post("/add_player/", json={"player_id": "Alice"})
    client.post("/add_player/", json={"player_id": "Bob"})
    response = client.post("/get_team_rating/", json={
        "team": ["Alice", "Bob"]
    })
    assert response.status_code == 200
    assert response.json() == {"team_rating": INITIAL_RATING}
