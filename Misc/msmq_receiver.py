import os
import json
import pythoncom
import win32com.client
from concurrent.futures import ThreadPoolExecutor


queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
queues = ['one']


def receive_messages(queue_name: str):

    queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
    queue = None

    try:
        queue = queue_info.Open(1, 0)

        while True:
            msgs = queue.Peek(pythoncom.Empty, pythoncom.Empty, 1000)
            if msgs:
                msg = queue.Receive()
                print(f'Got Message from {queue_name}: {msg.Label} - {msg.Body}')
            else:
                print(f'No more messages in {queue_name}')
                break
    except Exception as e:
        print(f'Error! {e}')

    finally:
        queue.Close()


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        for queue in queues:
            executor.submit(receive_messages, queue)


if __name__ == '__main__':
    main()


