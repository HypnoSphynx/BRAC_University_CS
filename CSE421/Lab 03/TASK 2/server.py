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

def count_vowles(message):
    vowels = "AEIOUaeiou"
    count = 0
    for char in message:
        if char in vowels:
            count += 1

    if count == 0:
        return "Not Enough Vowels"
    elif count<=2:
        return "Enough Vowels I guess"
    elif count>2:
        return "Too many vowels"


while True:
    connection, address = server.accept()
    connected= True

    print(f"Connection from {address} has been established!")
    while connected:
        initial_message = connection.recv(data).decode(format)
        if initial_message:
            message_length= int(initial_message)
            message= connection.recv(message_length).decode(format)
            print(f"Message from {address}: {message}")

            if message == termination_message:
                connection.send("Terminating".encode(format))
                print("Terminating connection", address)
                connected= False
            else:    
                response=count_vowles(message)
                connection.send(response.encode(format))
                print("Response sent")
    connection.close()


