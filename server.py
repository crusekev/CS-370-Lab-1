import socket

# Set the server's host IP address and port number
HOST = '10.0.0.1'
PORT = 65432

# Create a socket object with AF_INET (IPv4) and SOCK_STREAM (TCP) protocols
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port number
    s.bind((HOST, PORT))
    # Start listening for incoming connections
    s.listen()
    # Print a message indicating that the server is listening
    print('Server is listening on {}:{}'.format(HOST, PORT))
    conn, addr = s.accept()
    # Loop to receive and respond to messages
    with conn:
        print('Connected by', addr)
        while True:
            # Receive up to 1024 bytes of data from the client
            data = conn.recv(1024)
            if not data:
                break
            # Decode the received data and print it
            message = data.decode()
            print('Received message:', message)
            # Create a response message and send it back to the client
            response = 'Response from server: ' + message
            conn.sendall(response.encode())
            # Print a message indicating that the response has been sent
            print('Sent response:', response)
