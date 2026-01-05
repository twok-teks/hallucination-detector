from transformers import pipeline

def load_llm():
    return pipeline(
        "text-generation",
        model="distilgpt2"
    )

def ask(llm, prompt, max_length=50):
    formatted_prompt = f"Questions: {prompt}\nAnswer:"
    response = llm(formatted_prompt,
                   max_length=max_length,
                   do_sample = True,
                   temperature = 0.7)
    return response[0]["generated_text"]
