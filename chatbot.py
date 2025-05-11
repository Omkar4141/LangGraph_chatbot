from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

# -------------------------------
# 1. Define the State
# -------------------------------

class State(TypedDict):
    """
    The state of the graph. 
    - 'messages': a list of chat messages.
      The `add_messages` annotation ensures new messages are appended to the list
      instead of replacing it.
    """
    messages: Annotated[list, add_messages]


# Initialize the graph builder with the defined state type
graph_builder = StateGraph(State)


# -------------------------------
# 2. Import and Initialize LLM
# -------------------------------

import os
from langchain.chat_models import init_chat_model

# Set your API key for Google's Gemini model
os.environ["GOOGLE_API_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Initialize the chat model (Gemini 2.0 Flash)
llm = init_chat_model("google_genai:gemini-2.0-flash")


# -------------------------------
# 3. Define Node Logic
# -------------------------------

def chatbot(state: State) -> State:
    """
    A chatbot function node.
    It uses the LLM to generate a response based on the incoming messages.
    
    Args:
        state (State): Current graph state containing chat messages.
    
    Returns:
        State: Updated state with new assistant message appended.
    """
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# -------------------------------
# 4. Build the Graph
# -------------------------------

# Add the chatbot node to the graph
graph_builder.add_node("chatbot", chatbot)

# Define the edge from the start node to the chatbot node
graph_builder.add_edge(START, "chatbot")

# Compile the graph to make it ready for execution
graph = graph_builder.compile()


# -------------------------------
# 5. Stream Outputs from Graph
# -------------------------------

def stream_graph_updates(user_input: str):
    """
    Feeds user input into the graph and streams assistant responses.
    
    Args:
        user_input (str): The input text from the user.
    """
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


# -------------------------------
# 6. Run Chat Loop
# -------------------------------

if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except:
            # Fallback for environments without interactive input (like notebooks)
            user_input = "What do you know about LangGraph?"
            print("User:", user_input)
            stream_graph_updates(user_input)
            break
