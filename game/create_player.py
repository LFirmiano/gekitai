import socket
import asyncio
import threading

class Client():
    def __init__(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect(('localhost', 9000))

        print('Digite "quit" para terminar o chat')

        while True:
            try:
                client.send(input('Mensagem: ').encode('utf-8'))
                asyncio.ensure_future(self.handle_server_messages(client))
            except Exception as e:
                print(e)
                break
        try:
            client.close()
        except:
            exit(0)

    async def handle_server_messages(self, client):
        try:
            message = await client.recv(1024).decode('utf-8')
            print(message)
            if message == 'quit':
                client.close()
        except:
            pass