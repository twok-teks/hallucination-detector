from llm import load_llm, ask
def main():
    llm = load_llm()
    question = "Who was the first female president of the United States?"
    answer = ask(llm, question)
    print("Question: ", question)
    print("Answer: ", answer)

if __name__ == "__main__":
    main()