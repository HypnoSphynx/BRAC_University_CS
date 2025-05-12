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


def count_salary(hours):
    hours=int(hours)
    salary=0

    if hours<=40:
        salary= hours*200
    elif hours>40:
        salary= ((hours-40)*300)+8000
    return f"Total Hours: {hours}  Overtime: {hours-40} Salary: {salary}"

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

                response=count_salary(int(message))
                connection.send(response.encode(format))
                print("Response sent")

    connection.close()
