from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os 

def palmllm(query):
    load_dotenv(find_dotenv())
    api_key = os.environ['GOOGLE_API_KEY'] # put your API key here
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    print(response.text)
    return response.text
