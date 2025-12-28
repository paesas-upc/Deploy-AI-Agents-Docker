from langchain.agents import create_agent
from langgraph_supervisor import create_supervisor

from api.ai.llms import get_openai_llm

from api.ai.tools import (
    send_me_email,
    get_unread_emails,
    research_email
)

# EMAIL_TOOLS = {
#     "send_me_email": send_me_email,
#     "get_unread_emails": get_unread_emails
# }
# EMAIL_TOOLS_LIST = list(EMAIL_TOOLS.values())

EMAIL_TOOLS_LIST = [
    send_me_email,
    get_unread_emails
] # because we will probably want to add more tools to the list

def get_email_agent():
    model = get_openai_llm()
    agent = create_agent(
    model=model,
    tools=EMAIL_TOOLS_LIST,
    system_prompt="You are a helpful assistant for managing my email inbox for generating, sending and reviewing emails.",
    name='email_agent'
    )

    return agent

def get_research_agent():
    model = get_openai_llm()
    agent = create_agent(
    model=model,
    tools=[research_email],
    system_prompt="You are a helpful research assistant for preparing email data.",
    name='research_agent'
    )

    return agent

# supe = get_supervisor()
# supe.invoke({"messages": [{"role": "user", "content": "Find out how to create a latte then email me the results."}]})
def get_supervisor():
    llm = get_openai_llm()
    email_agent = get_email_agent()
    research_agent = get_research_agent()

    supe = create_supervisor(
        agents=[email_agent,research_agent],
        model=llm,
        prompt=(
            "You manage a research assistant and a"
            "email inbox manager assistant. Assign work to them"
        )
    ).compile()
    return supe