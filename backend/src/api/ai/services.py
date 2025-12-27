from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema


def generate_email_message(query:str) -> EmailMessageSchema:
    llm_base = get_openai_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema, method="json_mode")

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails. Always respond with a valid JSON object matching the required schema. The 'invalid_requests' field must be a boolean (true or false), NOT an array."
        ),
        ("human", f"{query}. Return ONLY a valid JSON object with 'subject', 'contents', and 'invalid_requests' fields. The 'invalid_requests' field must be a boolean (true or false), NOT an array.")
    ]
    return llm.invoke(messages)