
---

### Code Sample for Day 6
Below is a single Python file (`Day6_Samples_001.py`) with five sample programs tailored to Module 6: AI Integration (Days 26-30), focusing on Day 6's topics of introducing AI frameworks and simulating integration with ChatGPT and Grok. Note that real API integration requires valid API keys, which are simulated here with placeholders.

```python
# Day6_Samples_001.py
# Program 1: Setting Up Requests for API Calls
import requests
print("Requests library imported successfully.")

# Program 2: Simulated ChatGPT API Call
url = "https://api.openai.com/v1/chat/completions"  # Replace with actual endpoint
headers = {"Authorization": "Bearer YOUR_OPENAI_API_KEY"}  # Replace with your API key
data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Hello, how are you?"}]}
try:
    response = requests.post(url, json=data, headers=headers)
    print("ChatGPT Response:", response.json())
except Exception as e:
    print("Error:", e)

# Program 3: Simulated Grok API Call
url = "https://api.xai.com/v1/grok"  # Hypothetical endpoint
headers = {"Authorization": "Bearer YOUR_XAI_API_KEY"}  # Replace with your API key
data = {"query": "What is the weather like?"}
try:
    response = requests.post(url, json=data, headers=headers)
    print("Grok Response:", response.json())
except Exception as e:
    print("Error:", e)

# Program 4: Simple AI Response Simulation (No API)
def simulate_ai_response(query):
    responses = {"hello": "Hi there!", "weather": "It's sunny today!"}
    return responses.get(query.lower(), "I don't understand.")

print("Simulated Response:", simulate_ai_response("hello"))

# Program 5: Basic Chatbot Loop
while True:
    user_input = input("Ask something (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    response = simulate_ai_response(user_input)
    print("AI:", response)