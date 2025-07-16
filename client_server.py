import socket
import threading

def receive_msg(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:  # Connection closed
                break
            print(f"[SERVER] {msg}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            client.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('localhost', 5555))
        print("Connected to server!")
        
        receive_thread = threading.Thread(target=receive_msg, args=(client,))
        receive_thread.daemon = True  # Thread will exit when main program exits
        receive_thread.start()
        
        while True:
            msg = input("> ")
            client.send(msg.encode('utf-8'))
            if msg.lower() == "exit":
                break
                
    except ConnectionRefusedError:
        print("Server not available. Make sure the server is running first!")
    finally:
        client.close()
        print("Disconnected from server")

if __name__ == "__main__":
    start_client()