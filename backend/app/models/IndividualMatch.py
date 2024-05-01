from pydantic import BaseModel, Field

class IndividualMatch(BaseModel):
    player_a: str = Field(..., description="Identifier for player A")
    player_b: str = Field(..., description="Identifier for player B")
    score_a: float = Field(..., description="Score of player A (1 for win, 0.5 for draw, 0 for loss)",
                           ge=0, le=1)