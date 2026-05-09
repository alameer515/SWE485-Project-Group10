# api_config_template.py
# -------------------------------------------------------
# This is a TEMPLATE file. Do not add your actual API key here.
# To set up the API:
# 1. Create a file named .env in the project root
# 2. Add this line to it:  GROQ_API_KEY=your-actual-key-here
# 3. Get your free key from: https://console.groq.com
# 4. Make sure .env is listed in .gitignore (already done)
# -------------------------------------------------------

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

model_to_use = "llama-3.1-8b-instant"

## test the API connection runs successfully

try:
    response = client.chat.completions.create(
        model=model_to_use,
        messages=[
            {"role": "user", "content": "Hello! I am testing the Groq API connection for my university project."}
        ]
    )
    print("Success! Response:")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")