from printer import get_content
from datetime import datetime
from requests import post

start = datetime.now()

content = get_content(30)
this_message = f"Summarize this text:\n\n{content}"
content2 = {'messages':[{'content':this_message,'role':'user'}],'model':'ai/qwen2.5'}

this_response = post("http://172.17.0.1:12434/engines/v1/chat/completions",json=content2)

end = datetime.now()


print(content)
print('-----------------')
print(this_response.json()['choices'][0]['message']['content'])

print(f"Elapsed: {(end - start).total_seconds()} s")