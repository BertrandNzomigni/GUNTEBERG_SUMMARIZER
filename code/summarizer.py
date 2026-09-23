from text_loading import get_content
from datetime import datetime
from transformers import AutoModelForCausalLM,AutoTokenizer, pipeline


start = datetime.now()


model = AutoModelForCausalLM.from_pretrained("/code/model")
tokenizer = AutoTokenizer.from_pretrained("/code/model")

summarization = pipeline("text-generation", model=model,tokenizer=tokenizer)
content = get_content(30)
messages = [{"role": "user", "content": f"Summarize this text:\n\n{content}"}]



summary_text = summarization(messages,max_new_tokens=200)[0]["generated_text"][-1]["content"]

end = datetime.now()

print(content)
print('-----------------')
print(summary_text)

print(f"Elapsed: {(end - start).total_seconds()} s")