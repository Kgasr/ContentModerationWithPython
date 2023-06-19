import os
from Configuration import config
from ExternalAPI import api_client
from Core.get_handler import get_handler
from Core.formatter import format_input, format_output

def moderation_call(messages):
    moderation_flag = ""
    if messages:
        for msg in messages:
            for key in msg:
                moderation_flag = api_client.openai_api_call(msg[key])
            msg.update({'moderation_status':moderation_flag})
        return messages

def moderate():
    keys = {"source_type"}
    config_pairs = config.get_config(keys)
    source_type = config_pairs["source_type"]
    source = config_pairs["source"]

    handler = get_handler(source_type, source)
    messages = handler.get_data()
    print(messages)
    formatted_messages = format_input(messages, source_type)
    print(formatted_messages)
    """
    output = moderation_call(formatted_messages)
    formatted_output = formatter.format_output(messages, formatted_messages, output, source_type)
    handler.set_data(formatted_output)
    """
