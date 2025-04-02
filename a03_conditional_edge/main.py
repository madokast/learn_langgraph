from typing import Dict, Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END

NodeId = str

def merge_dicts(old: Dict, new: Dict) -> Dict:
    """深度合并字典"""
    merged = old.copy()
    for k, v in new.items():
        if isinstance(v, dict) and k in merged and isinstance(merged[k], dict):
            merged[k] = merge_dicts(merged[k], v)
        else:
            merged[k] = v
    return merged

class MyState(TypedDict):
    values: Annotated[Dict[NodeId, int], merge_dicts] 

def add_one_to_start(state: MyState):
    # add_one_to_start {'values': {'__start__': 123}}
    print("add_one_to_start", state)
    if "add_one_to_start" in state["values"]:
        # 如果已经存在值，则加 1
        state["values"]["add_one_to_start"] += 1
    else:
        state["values"]["add_one_to_start"] = state["values"].get(START, 0) + 1
    return state

def route(state: MyState):
    print("route", state)
    # 值大于 10 才能到达 END
    if state["values"]["add_one_to_start"] > 10:
        return END
    return "add_one_to_start"

graph_builder = StateGraph(MyState)
graph_builder.add_node("add_one_to_start", add_one_to_start)
graph_builder.add_edge(START, "add_one_to_start")
graph_builder.add_conditional_edges("add_one_to_start", route)
graph = graph_builder.compile()

def stream_graph_updates(init_value: int):
    result = graph.invoke(MyState(values={START: init_value}))
    # {'values': {'__start__': 123, 'add_one_to_start': 124}}
    print("result", result)

if __name__ == "__main__":
    user_input = "hi!"
    stream_graph_updates(5)
