from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest", max_tokens=75)


while True:
    prompt = input("you: ")
    if prompt == "0":
        print("Chat bot Deactivated")
        break
    response = model.invoke(prompt)
    print("bot: ",response.content)
print("test completed")