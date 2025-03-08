import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def draft_answer(research: str) -> dict:
    """Structure research data into a user-friendly response"""
    response = model.generate_content(research)

    # ✅ Extract the response text properly
    if hasattr(response, "text"):
        response_text = response.text
    else:
        response_text = str(response)  # Convert to string if needed

    return {"response": response_text}  # ✅ Ensure a dictionary return
