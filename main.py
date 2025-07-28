from agents import Agent, Runner
from connection import get_config
from utils import save_translation

agent = Agent(
    name="translator",
    instructions="You are a helpful translator. Always translate into Urdu."
)

print("📘 Type something in English to translate it to Urdu. Type 'exit' to quit.\n")

while True:
    user_input = input("🗣️  You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    result = Runner.run_sync(agent, user_input, run_config=get_config())
    print(f"🤖 Translator: {result.final_output}\n")
    save_translation(original=user_input, translated=result.final_output, language="Urdu")
