import os, json, requests, warnings
from dotenv import load_dotenv
from os.path import join, dirname
from urllib3.exceptions import InsecureRequestWarning
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def SampleCall(message):
    dotenv_path = join(dirname(__file__), 'back.env')
    load_dotenv(dotenv_path)
    api_key = os.getenv('openai_api_key')
    api_url = os.getenv('openai_api_url')
    engine = os.getenv('engine')
    temperature = int(os.getenv('temperature'))
    max_tokens = int(os.getenv('max_tokens'))
    return requests.post(api_url,
                             headers={"Content-Type": "application/json","Authorization": f"Bearer {api_key}"},
                             json={"prompt": message,"temperature": temperature,"max_tokens": max_tokens},
                             verify=False)
def main():
    prompt = input("********** Please provide the prompt for OpenAI API Call ********** \n")
    result = SampleCall(prompt)
    if result.status_code != 200:
        print("Error:", result.status_code, result.content)
    else:
        results = result.json()['choices'][0]['text']
        print("\n\n ********** OpenAI API Call Response **********")
        print(results)
        print("\n\n **********************************************")
if __name__ == '__main__':
    main()


