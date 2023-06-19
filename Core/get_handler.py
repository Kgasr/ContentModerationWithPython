from Handlers import api_handler,msmq_handler,text_file_handler

def get_handler(source_type, source):
    try:
        if source_type == 'msmq':
            handler = msmq_handler.MsmqHandler(source)
        elif source_type == 'txt':
            handler = text_file_handler.TxtFileHandler(source)
        elif source_type == 'api':
            handler = api_handler.ApiHandler(source)
        else:
            raise Exception("Source Not Supported")
        return handler
    except Exception as ex:
        raise Exception(str(ex))