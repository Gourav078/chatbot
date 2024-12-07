
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,

)

history =[]
print("Chintu: Hello How Are you I Am Your Friendly ChatBot")

while True:
  user_input = input("you:")

  chat_session = model.start_chat(
    history=history

  )

  response = chat_session.send_message(user_input)

  # print(response.text)
  model_response = response.text

  print(f'Chintu:{model_response}')


  # print()

  history.append({"role": "user", "parts":[user_input]})

  history.append({"role": "model", "parts":[model_response]})
