# api_config_template.py
# -------------------------------------------------------
# This is a TEMPLATE file. Do not add your actual API key here.
# To set up the API:
# 1. Create a file named .env in the project root
# 2. Add this line to it:  GEMINI_API_KEY=your-actual-key-here
# 3. Get your free key from: https://aistudio.google.com
# 4. Make sure .env is listed in .gitignore (already done)
# -------------------------------------------------------

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Loads key from .env file

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Test connection (optional)
# response = model.generate_content("Hello")
# print(response.text)