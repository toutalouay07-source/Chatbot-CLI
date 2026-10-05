
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
import threading
import time
import sys

llm = ChatOpenAI(
    base_url="http://192.168.0.183:1234/v1",  # URL du serveur LM Studio
    api_key="lm-studio",                  # n'importe quelle valeur
    model="google/gemma-4-e2b"
)

def spinner(stop_event):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\rBot pense... {frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * 30 + "\r")  # efface la ligne
    sys.stdout.flush()

historique=[
    SystemMessage(content="You are AI assistance You must answer briefly 10 word or 20 word.")
]
print("Chatbot~Local! Tape <<exit>> to leave ")

while True:
    user_message = input("TOI: ")

    if user_message.lower() in ["exit"]:
        print("🤖: Au revoir 👋")
        break

    historique.append(HumanMessage(content=user_message))

    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event,))
    t.start()

    response = llm.invoke(historique)

    stop_event.set()
    t.join()

    historique.append(AIMessage(content=response.content))

    print(f"🤖: {response.content}")