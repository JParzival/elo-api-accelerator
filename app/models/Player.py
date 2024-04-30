from pydantic import BaseModel, Field

class Player(BaseModel):
    player_id: str = Field(..., description="Unique identifier for the player")