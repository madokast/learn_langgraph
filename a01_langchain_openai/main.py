"""
学习怎么使用 langchain-openai
中转 https://yunwu.ai
模型名 gpt-4o-mini
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

API_KEY = "sk-ZOfOKeGY98i7YaGWMoIaayvmkZiQ4Yx8t7GXDSWy7vsSWdMl" # 2025年4月3日 过期

model = ChatOpenAI(
        model="gpt-4o-mini",
        # 踩坑，需要加上 /v1
        openai_api_base="https://yunwu.ai/v1",
        openai_api_key=API_KEY
    )


messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="hi!"),
]

response = model.invoke(messages)
print(response)
"""
content='你好!' additional_kwargs={'refusal': None} response_metadata={'token_usage': 
{'completion_tokens': 3, 'prompt_tokens': 20, 'total_tokens': 23, 'completion_tokens_details': 
{'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 
'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 
'system_fingerprint': 'fp_b705f0c291', 'id': 'chatcmpl-BHlhc9UDILpJaHPTDcey9d7wLNH3g', 
'finish_reason': 'stop', 'logprobs': None} id='run-2ea476dd-4be7-4e0f-b154-484d79e5ecff-0' 
usage_metadata={'input_tokens': 20, 'output_tokens': 3, 'total_tokens': 23, 'input_token_details': 
{'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""