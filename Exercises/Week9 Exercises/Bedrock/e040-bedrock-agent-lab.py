from pydantic import BaseModel, Field
from langchain_core.tools import tool
#from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_ollama import ChatOllama


# =====================================================================
# 1. Pydantic Structured Output Schema
# =====================================================================
# TODO: Define a 'StockRecommendation' class inheriting from BaseModel.
# Fields:
#   - ticker (str): The stock ticker (e.g. "TSLA")
#   - recommendation (str): "BUY", "SELL", or "HOLD"
#   - reasoning (str): A one-sentence justification.
class StockRecommendation(BaseModel):
    ticker: str
    recommendation: str
    reasoning: str

# =====================================================================
# 2. Tool Definition
# =====================================================================
# TODO: Define a @tool function named 'get_stock_sentiment'.
# It should accept 'ticker: str' and return a str.
# Write a clear docstring — the LLM reads it to know when to call this tool.
# Include mock sentiment data for at least 3 tickers (AAPL, TSLA, AMZN).

# @tool
# def get_stock_sentiment(ticker: str) -> str:
#     """..."""
#     pass

@tool
def get_stock_sentiment(ticker: str) -> str:
    """use this tool to get the sentiment of a given stock, for example: AAPL, TSLA, AMZN"""
    mock_data = {
        "AAPL": "SELL",
        "TSLA": "HOLD",
        "AMZN": "BUY",
    }
    return mock_data.get(ticker, "Ticker not found")


# =====================================================================
# 3. Agent Initialization
# =====================================================================
# TODO: Use init_chat_model() to initialize Amazon Bedrock.
# Use model="us.anthropic.claude-3-5-sonnet-20240620-v1:0"
# Use model_provider="bedrock" and temperature=0

# llm = init_chat_model(...)
#llm = init_chat_model(
#    model="mistral.ministral-3-8b-instruct",
#    model_provider="bedrock",
#    temperature=0,
#)
# create new llm model using Ollama instead of bedrock
llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)
# =====================================================================
# 4. Create the ReAct Agent
# =====================================================================
# TODO: Use create_react_agent with your llm, tools list, and a
# professional financial-analyst system_prompt (via state_modifier).

# agent = create_react_agent(...)
# changed system prompt to save tokens
system_prompt = """You are a financial analyst.
- Use the tool if needed
- Respond in 1–2 sentences max
- Do NOT explain your reasoning steps
"""
agent = create_agent(model=llm, tools=[get_stock_sentiment], system_prompt=system_prompt)
# =====================================================================
# 5. Stream the Agent Response
# =====================================================================
def run_exercise():
    query = {"messages": [("user", "What is your recommendation for Tesla (TSLA) stock?")]}
    
    # TODO: Stream the agent using .stream(query, stream_mode="values")
    # For each chunk, print the last message's type and content.
    print("=== e040: Your First Bedrock Agent ===")
    # YOUR CODE HERE
    result = agent.invoke(query)
    
    print(result["messages"][-1].content)

if __name__ == "__main__":
    run_exercise()
