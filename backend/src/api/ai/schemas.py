import os

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class EmailMessageSchema(BaseModel):
    subject: str
    contents: str
    invalid_requests: bool | None = Field(default=False)