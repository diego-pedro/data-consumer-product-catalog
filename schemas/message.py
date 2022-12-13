"""Message input between services."""

from pydantic import BaseModel


class MessageInput(BaseModel):
    content: str

    class Config:
        """Enable object relational mapping"""
        orm_mode = True