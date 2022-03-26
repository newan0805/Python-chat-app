import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 4226))

print('Client engaging to server...')

while True:    
    msg = input("Type your message: ")
    client.send(msg.encode('utf-8'))

    if msg == 'quite':
        break
    elif msg == 'q':
        break
    
    msg = client.recv(1024).decode('utf-8')
    print("SERVER MESSAGE \t", msg)
