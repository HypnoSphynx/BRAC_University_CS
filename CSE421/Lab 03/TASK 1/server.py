import socket
format= 'utf-8'
port= 5050
data=16
termination_message= "close"
hostname = socket.gethostname()
host_address = socket.gethostbyname(hostname)

server_socket_address = (host_address, port)
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)
server.listen()

print(f"Server is listening on {host_address}:{port}")


while True:
    connection, address = server.accept()
    connected= True

    print(f"Connection from {address} has been established!")

    while connected:
        initial_message = connection.recv(data).decode(format)
        if initial_message:
            message_length= int(initial_message)
            message= connection.recv(message_length).decode(format)

            if message == termination_message:
                connection.send("Terminating".encode(format))
                print("Terminating connection", address)
                connected= False
            else:    
                print(f"Message from {address}: {message}")
                connection.send("Message received".encode(format))
    connection.close()
