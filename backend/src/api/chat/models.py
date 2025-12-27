from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime, timezone

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessagePayload(SQLModel):
    # pydantic model
    # validation
    # serializer
    message: str

# comment
class ChatMessage(SQLModel, table=True): # type: ignore
    # database table
    # saving, updating, getting, deleting
    # serializer
    id: int | None = Field(default=None, primary_key=True) # 1, 2, 3, 4...
    message: str
    created_at: datetime = Field(
        default=get_utc_now(),
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False,
    )

class ChatMessageList(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)