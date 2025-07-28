# 📁 Project Structure: hello-open-ai-agent


hello-open-ai-agent/
├── .env                      # Stores GEMINI_API_KEY
├── connection.py            # Creates and exports RunConfig with Gemini
├── tool.py                  # Custom tool: translate_to(lang, text)
├── utils.py                 # History save/load helpers
├── main.py                  # Synchronous translator agent
├── async_main.py            # Asynchronous translator agent
├── history.json             # Translation history (auto-created)
└── requirements.txt         # Project dependencies



# sultan-translator-history
