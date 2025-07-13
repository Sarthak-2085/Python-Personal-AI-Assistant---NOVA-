# Both open ai and gemini api key are not working, so I am commenting them out.      


  # !!! Open Ai requires money to use their API , insted use Gemini !!!

# from openai import OpenAI
 
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="your api key here",
# ) #Replace with your OpenAI API key

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named nova skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)

                            

                                # !!! Gemini API !!!

# pip install google-generativeai

# import google.generativeai as genai

# # Replace this with your actual Gemini API key
# genai.configure(api_key="you Api key here ")

# #  Correct model name with "models/" prefix
# model = genai.GenerativeModel("models/gemini-pro")

# response = model.generate_content([
#     "You are a virtual assistant named nova skilled in general tasks like Alexa and Google Cloud.",
#     "What is coding?"
# ])

# print(response.text)


