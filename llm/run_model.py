from transformers import AutoTokenizer, AutoModel, PreTrainedModel

model_path = "llm/models/gpt_2"
model_name = "openai-community/gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model: PreTrainedModel = AutoModel.from_pretrained(model_path)

inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)
print(outputs)
