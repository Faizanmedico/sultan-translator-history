import asyncio

from agents import Agent, Runner
from connection import get_config
from utils import save_translation # Make sure utils.py exists and save_translation is defined there

# Define the agent
# IMPORTANT: Assign the model from get_config() to the agent
translator = Agent(
    name="translator",
    instructions="You are a helpful translator. Always translate into Urdu.",
    model=get_config().model # <--- This was missing!
)

async def main():
    print("\n📚 Type something in English to translate it to Urdu. Type 'exit' to quit.\n")
    conversation_history = [] # To keep track of the conversation

    while True:
        question = input("🗣️  You: ") # Use a clearer emoji for input
        if question.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye!") # Use a clearer emoji for goodbye
            break

        # Construct the full prompt including conversation history
        # This sends the entire context to the model for each turn
        full_prompt = "\n".join(conversation_history + [f"User: {question}"])

        # Run the translator agent asynchronously with the prompt and run_config
        result = await Runner.run(translator, full_prompt, run_config=get_config())

        # Print the translated output
        print(f"🤖 Translator: {result.final_output}\n") # Use a clearer emoji for bot

        # Append current turn to conversation history
        conversation_history.append(f"User: {question}")
        conversation_history.append(f"Translator: {result.final_output}")

        # Save the translation - make sure this is correctly indented and uses 'question'
        save_translation(original=question, translated=result.final_output, language="Urdu")


if __name__ == "__main__":
    asyncio.run(main())
    