import random
import socket

class GuessingGameServer:
    def __init__(self, host="0.0.0.0", port=7777):
        self.host = host
        self.port = port
        self.secret_number = random.randint(1, 100)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connected by {addr}")
            with conn:
                attempts = 0  # Initialize attempts counter
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break
                    try:
                        guess = int(data)
                        attempts += 1  # Increment attempt counter
                        if guess < self.secret_number:
                            response = f"Too low! Attempt: {attempts}"
                        elif guess > self.secret_number:
                            response = f"Too high! Attempt: {attempts}"
                        else:
                            # Determine the message based on attempts
                            if attempts <= 5:
                                performance = "Very good"
                            elif 6 <= attempts <= 10:
                                performance = "Good"
                            else:
                                performance = "Fair"
                            response = f"Correct! You win! Total attempts: {attempts}. {performance}"
                            self.secret_number = random.randint(1, 100)  # Reset for next game   
                        conn.sendall(response.encode())
                    except ValueError:
                        conn.sendall("Invalid input! Please enter a number.".encode())
                    
    def stop(self):
        self.server_socket.close()

def main():
    server = GuessingGameServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.stop()

if __name__ == "__main__":
    main()
