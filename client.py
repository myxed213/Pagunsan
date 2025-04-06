import socket

class GuessingGameClient:
    def __init__(self, host="10.125.9.12", port=7777):
        self.host = host
        self.port = port

    def play(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            print("Connected to the server. Guessing numbers...")
            
            low, high = 1, 100
            while low <= high:
                guess = (low + high) // 2 
                print(f"Guessing: {guess}")
                client_socket.sendall(str(guess).encode())
                response = client_socket.recv(1024).decode()
                print(response)
                
                if "Correct! You win!" in response:
                    print("Game over. The correct number was found!")
                    break  
                elif "too high" in response.lower():
                    high = guess - 1
                elif "too low" in response.lower():
                    low = guess + 1

            input("Press Enter to exit...") 

def main():
    client = GuessingGameClient()
    try:
        client.play()
    except KeyboardInterrupt:
        print("Stopping client.")
    finally:
        pass

if __name__ == "__main__":
    main()
