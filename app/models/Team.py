from pydantic import BaseModel, Field
from typing import List  # Import List from typing if Python <3.9

class Team(BaseModel):
    team: List[str] = Field(..., description="List of player identifiers in the team")