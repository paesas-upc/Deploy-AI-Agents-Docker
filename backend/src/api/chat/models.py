from sqlmodel import SQLModel, Field


class ChatMessagePayload(SQLModel):
    # pydantic model
    # validation
    # serializer
    message: str

class ChatMessage(SQLModel, table=True): # type: ignore
    # database table
    # saving, updating, getting, deleting
    # serializer
    id: int | None = Field(default=None, primary_key=True) # 1, 2, 3, 4...
    message: str