from printer import get_content
from datetime import datetime


start = datetime.now()

from transformers import pipeline

summarization = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")
content = get_content(30)
messages = [{"role": "user", "content": f"Summarize this text:\n\n{content}"}]



summary_text = summarization(messages,max_new_tokens=200)[0]["generated_text"][-1]["content"]

end = datetime.now()

print(content)
print('-----------------')
print(summary_text)

print(f"Elapsed: {(end - start).total_seconds()} s")