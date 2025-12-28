from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.db import get_session
from api.ai.agents import get_supervisor
from api.ai.schemas import EmailMessageSchema, SupervisorMessageSchema
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
# curl.exe -X POST -H "Content-Type: application/json" -d '{\"message\": \"Hello world\"}' https://ai-agents-docker-production.up.railway.app/api/chats/

#  curl.exe -X POST -H "Content-Type: application/json" -d '{\"message\": \" Give me a summary of why it is good to go outside\"}' https://ai-agents-docker-production.up.railway.app/api/chats/

#  curl.exe -X POST -H "Content-Type: application/json" -d '{\"message\": \" Research who is Jon Snow and email me the results\"} http://localhost:8080/api/chats/
@router.post("/", response_model=SupervisorMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session) 
    ):
    data = payload.model_dump() # pydantic -> dict
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj) 
    session.commit()

    supe = get_supervisor()
    msg_data = {
        "messages": [
            {"role": "user",
             "content": f"{payload.message}"
             },
        ]
    }
    result = supe.invoke(msg_data)
    if not result:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    messages = result.get("messages")
    if not messages:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    return messages[-1]