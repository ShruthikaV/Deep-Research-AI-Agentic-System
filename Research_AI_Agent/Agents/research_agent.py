import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def fetch_information(query):
    if isinstance(query, tuple):  # Ensure query is a string
        query = query[1]  
    query = str(query).strip() 
    print(f"Query type: {type(query)}, Query value: {query}")
    response = model.generate_content(query)
    return response.text  # Adjust based on the response format










