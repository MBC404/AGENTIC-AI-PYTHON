import google.generativeai as genai
import os
os.environ["MY_GEMINI_API_KEY"] = ""   #use your api key here
from google.generativeai import types
os.getenv("MY_GEMINI_API_KEY")
genai.configure(api_key=os.environ["MY_GEMINI_API_KEY"])


model = genai.GenerativeModel('gemini-1.5-flash-latest')
config = types.GenerationConfig(
max_output_tokens=100,
temperature=0.2
)

response = model.generate_content(
"write an essay about rains",
generation_config=config
)
print(response.text)
