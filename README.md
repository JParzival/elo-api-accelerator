# 🚴 Elo API Accelerator

The aim of this project is to help accelerate the creation of an Elo System using Python, FastAPI and Streamlit.

Currently working for Python < 3.9, conversion to superior versions is straightforward. 

<br />

# 👍 Benefits of this project

- Currently working with FastAPI
- Basic functionality and endpoints already running
- Prepared for developing connection to databases
- Postman collection included for demonstration purposes
- Frontend in Streamlit connected to the API for user-friendly usage

<br />

# 🦾 Example of usage
## *API - Backend*
 ### Run the API

 1. Install the requirements (proper environment with FastAPI and Uvicorn setup)
 2. Go to the app folder `cd backend/app`
 3. Run the server: `uvicorn main:app --reload`
 4. Access the endpoints via POST and GET requests to the server's URL.


 ### Run tests
 1. Go to the tests folder `cd backend/tests`
 2. Adjust the sys.path in the code to your main.py location
 3. Run pytest

<br />

## *Frontend*
 ### Run the frontend
 1. Make sure that streamlit is installed with the requirements
 2. Go to the frontend folder `cd frontend`
 3. Run the frontend: `streamlit run frontend.py`
