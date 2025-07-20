import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get('gemini_key'))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def generate_code(prompt):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You have to act as a system named 'Jarvis' that only generates single file code or program in given programming language for given prompt that is requests by user. ",
    )
    
    response  = model.generate_content(prompt)
    return response.text

# print(generate_code("write a code for addition in c"))
