from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

def chatbot(state: State):
    print("node chatbot received state:", state)
    print("node chatbot received state messages:", state["messages"])
    """
    node chatbot received state: {'messages': [HumanMessage(content='hi!', additional_kwargs={}, response_metadata={}, id='0574134b-1abd-4b13-aa42-f03075c0393a')]}
    node chatbot received state messages: [HumanMessage(content='hi!', additional_kwargs={}, response_metadata={}, id='0574134b-1abd-4b13-aa42-f03075c0393a')]
    """
    return {"messages": ["the answer is ......"]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.invoke(State(messages=[{"key1": "value1", "content": user_input}])):
        # stream get event: {'chatbot': {'messages': ['the answer is ......']}}
        print("stream get event:", event)
        for value in event.values():
            print("Assistant:", value["messages"][-1])

if __name__ == "__main__":
    user_input = "hi!"
    stream_graph_updates(user_input)

"""
graph.stream 输入 {"messages": [{"role": "user", "content": user_input, "the another key": "some value"}]}
chatbot 获得 messages: [HumanMessage(content='hi!', additional_kwargs={'the another key': 'some value'}, response_metadata={}, id='7e41f44f-2021-41d3-8687-d537afbd1143')]
"""