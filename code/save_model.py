from transformers import AutoModelForCausalLM,AutoTokenizer


AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct").save_pretrained("/code/model")
AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct").save_pretrained("/code/model")