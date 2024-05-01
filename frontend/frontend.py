import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"  # Where the API is

def add_player(player_id):
    response = requests.post(f"{API_BASE_URL}/add_player/", json={"player_id": player_id})
    return response.json()

def get_player_rating(player_id):
    response = requests.get(f"{API_BASE_URL}/get_rating/player_id={player_id}")
    return response.json()

def update_individual_match(player_a, player_b, score_a):
    response = requests.post(f"{API_BASE_URL}/update_individual_match/", json={
        "player_a": player_a,
        "player_b": player_b,
        "score_a": score_a
    })
    return response.json()

def update_team_match(team_a, team_b, score_a):
    response = requests.post(f"{API_BASE_URL}/update_team_match/", json={
        "team_a": team_a,
        "team_b": team_b,
        "score_a": score_a
    })
    return response.json()

def get_team_rating(team):
    response = requests.post(f"{API_BASE_URL}/get_team_rating/", json={"team": team})
    return response.json()

## Frontend itself

st.title('Elo Rating System')

st.header('Add a new Player')
player_id = st.text_input('Enter player ID to add:')
if st.button('Add Player'):
    result = add_player(player_id)
    st.write(result)

st.header('Get Player Rating')
player_id_rating = st.text_input('Enter player ID to get rating:')
if st.button('Get Rating'):
    try:
        result = get_player_rating(player_id_rating)
        st.write(f"Rating of {player_id_rating}: {result['rating']}")
    except:
        st.write("Failed to get player rating. Is the player added?")

st.header('Update Individual Match')
player_a = st.text_input('Player A ID:')
player_b = st.text_input('Player B ID:')
score_a = st.number_input('Score for Player A (1 win, 0.5 draw, 0 loss):', min_value=0.0, max_value=1.0, value=0.5, step=0.5)
if st.button('Update Match'):
    result = update_individual_match(player_a, player_b, score_a)
    st.write(result)

st.header('Update Team Match')
team_a = st.text_input('Team A IDs (comma-separated):').split(',')
team_b = st.text_input('Team B IDs (comma-separated):').split(',')
team_score_a = st.number_input('Score for Team A (1 win, 0.5 draw, 0 loss):', min_value=0.0, max_value=1.0, value=0.5, step=0.5)
if st.button('Update Team Match'):
    result = update_team_match(team_a, team_b, team_score_a)
    st.write(result)

st.header('Get Team Rating')
team_rating = st.text_input('Enter team IDs to get rating (comma-separated):').replace(', ', ',').split(',')
if st.button('Get Team Rating'):
    try:
        result = get_team_rating(team_rating)
        st.write(f"Average Rating of Team: {result['team_rating']}")
    except:
        st.write("Failed to get team rating. Is everything written okay?")
