from pydantic import BaseModel, Field
from typing import List  # Import List from typing if Python <3.9

class TeamMatch(BaseModel):
    team_a: List[str] = Field(..., description="List of player identifiers representing team A")
    team_b: List[str] = Field(..., description="List of player identifiers representing team B")
    score_a: float = Field(..., description="Score of team A (1 for win, 0.5 for draw, 0 for loss)",
                           ge=0, le=1)