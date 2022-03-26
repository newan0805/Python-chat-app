import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 4226))
server.listen()

print("Waitin for a client...")
client,addr = server.accept()
print(f"Client Address {addr}")

while True:    
    msg = client.recv(1024).decode('utf-8')
    print("CLIENT MESSAGE \t", msg)

    if msg == 'quite':
        break
    elif msg == 'q':
        break
    
    msg = input("Type your message: ")
    client.send(msg.encode('utf-8'))
