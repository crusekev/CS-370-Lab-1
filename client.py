import socket

# Set the server's host IP address and port number
HOST = '10.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server at the specified host and port number
    s.connect((HOST, PORT))
    # Prompt user for a message
    message = input('Enter a message to send to the server: ')
    # Send the message to the server
    s.sendall(message.encode())
    # Print a message indicating that the message has been sent
    print('Sent message:', message)
    # Receive up to 1024 bytes of data from the server
    data = s.recv(1024)
    # Decode the received data and print it
    response = data.decode()
    print('Received response:', response)

