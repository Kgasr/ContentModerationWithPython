from Configuration import config
import requests

def openai_api_call(message):
    try:
        keys = {"api_url", "api_key", "temperature", "max_tokens"}
        config_pairs = config.get_config(keys)

        api_url = config_pairs["api_url"]
        api_key = config_pairs["api_key"]
        temperature = config_pairs["temperature"]
        max_tokens = config_pairs["max_tokens"]

        response = requests.post(api_url,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {api_key}"},
                                 json={
                                     "input": message,
                                     "temperature": temperature,
                                     "max_tokens": max_tokens,
                                     "stop": ["###"]
                                 },
                                 verify=False)
        if response.status_code != 200:
            results = "Error"
            # print("Error:", response.status_code, response.content)
            # response_dict = json.loads(response.content.decode('utf-8'))
            # error_message = response_dict['error']['message']
            # results = {'Prompt': message, 'Error code ': response.status_code , 'Error message ': error_message}
        else:

            results = response.json()['results'][0]['flagged']
            # results = {'Prompt': message, 'Moderation Flag': output}
            # print(results)
        # print(results)
        return results
    except Exception as ex:
        raise Exception(str(ex))
