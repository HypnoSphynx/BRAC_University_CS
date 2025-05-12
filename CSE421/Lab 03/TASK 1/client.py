import socket


format= 'utf-8'
port=5050
data=16
termination_message= "close"
hostname = socket.gethostname()
host_address = socket.gethostbyname(hostname)

server_socket_address = (host_address, port)
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_socket_address)

def message_server(message):

    message=str(message).encode(format)
    message_length=len(message)
    send_length=str(message_length).encode(format)
    send_length+=b' '*(data-len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format)) 


message_server(f"Client's IP address: {host_address}")
message_server(f"Client's Device name: {hostname}")
message_server(termination_message)