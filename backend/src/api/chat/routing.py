from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from .models import ChatMessagePayload, ChatMessage, ChatMessageList
router = APIRouter()

# /api/chats/
@router.get("/")
def chat_health():
    return {"status":"ok"}

# /api/chats/recent/
# curl.exe http://localhost:8080/api/chats/recent/
@router.get("/recent/", response_model=List[ChatMessageList])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results

# HTTP POST -> payload = {"message":"Hello world"} -> {"message": "hello world", "id": 1}
# curl.exe -X POST -H "Content-Type: application/json" -d '{\"message\": \"Hello world\"}' http://localhost:8080/api/chats/
# curl.exe -X POST -H "Content-Type: application/json" -d '{\"message\": \"Hello world\"}'  https://ai-agents-docker-production.up.railway.app/api/chats/

#  curl.exe -X POST http://localhost:8080/api/chats/ -H "Content-Type: application/json" -d '{\"message\": \" Give me a summary of why it is good to go outside\"}' 
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session) 
    ):
    data = payload.model_dump() # pydantic -> dict
    print(data)
    obj = EmailMessageSchema.model_validate(data)
    session.add(obj) 
    session.commit()
    # session.refresh(obj) # ensure id/primary key is added to the obj instance
    # ready to store in the db
    response = generate_email_message(payload.message)
    return obj