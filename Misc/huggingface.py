import requests

def complete_text(prompt):
    # Hugging Face API endpoint
    url = "https://api-inference.huggingface.co/models/gpt2"

    # Request payload
    payload = {
        "inputs": "c# code to search an array for an element",
        "parameters": {
            "max_new_tokens": 200
        }
    }

    # Request headers
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    # Make the API requestq
    response = requests.post(url, json=payload, headers=headers, verify=False)

    # Check the response status code
    if response.status_code == 200:
        # Extract the completed text from the response

        print(response.json())
        completed_text = response.json()[0]['generated_text']
        return completed_text
    else:
        print("Request failed with status code:", response.status_code)
        return None

# Prompt for user input
prompt = input("Enter the text prompt: ")

# Call the complete_text function
completed_text = complete_text(prompt)

# Print the completed text
print("Completed Text:")
print(completed_text)



'''
from transformers import pipeline
import torch

# Load the pre-trained sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis", verify = False)

# Example sentence for sentiment analysis
sentence = "I love using Hugging Face!"

# Perform sentiment analysis
results = sentiment_analysis(sentence)

# Display the sentiment and confidence score
for result in results:
    print(f"Sentiment: {result['label']}")
    print(f"Confidence Score: {result['score']}")
'''

'''

import requests

# Disable SSL certificate verification
#requests.packages.urllib3.disable_warnings()

# Make the request with SSL verification disabled
response = requests.get("https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english/resolve/main/config.json", verify=False)

# Print the response content
print(response.json())
'''