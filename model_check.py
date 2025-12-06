import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBLoWUfXZWtIbMXigRwEcDtETSDGxTg_JE")

for m in genai.list_models():
    print(m.name)
