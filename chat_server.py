import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if not msg or msg.lower() == "disconnect":  # Fixed typo and added case-insensitive check
                connected = False
            else:
                print(f"[{addr}] {msg}")  # Added space for better formatting
                conn.send("Message received".encode('utf-8'))  # Fixed capitalization
        except ConnectionResetError:
            print(f"[{addr}] Connection lost unexpectedly")
            connected = False
    conn.close()
    print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse
    try:
        server.bind(('localhost', 5555))
        server.listen()
        print("[SERVER] Server is listening...")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))  # Fixed 'arg' to 'args'
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Fixed typo "CONNECTIONS"
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down server...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()