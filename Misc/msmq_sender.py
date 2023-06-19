import os
import time
import random
import win32com.client

queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
queues = ['one']

def send(queue_name: str, label: str, message: str):
    queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
    queue = None
    try:
        queue = queue_info.Open(2, 0)
        msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        msg.Label = label
        msg.Body = message
        msg.Send(queue)
    except Exception as e:
        print(f'Error! {e}')
    finally:
        queue.Close()

def main():
    i = 0
    while i<1:
        print(i)
        i += 1
        send(random.choice(queues), 1, 'I will kill you')
        send(random.choice(queues), 2, 'I love you')
        print(f'{i}: Message sent!')
        time.sleep(0.5)


if __name__ == '__main__':
    main()