import tkinter as tk  # Changed from _tkinter to tkinter
import socket
import threading

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chat App")
        
        # Initialize client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # GUI Elements
        self.chat_frame = tk.Frame(root)
        self.scrollbar = tk.Scrollbar(self.chat_frame)
        self.chat_list = tk.Listbox(
            self.chat_frame, 
            height=15, 
            width=50, 
            yscrollcommand=self.scrollbar.set
        )
        self.scrollbar.config(command=self.chat_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_list.pack(side=tk.LEFT, fill=tk.BOTH)  # Fixed tk.both to tk.BOTH
        self.chat_frame.pack()
        
        self.msg_entry = tk.Entry(root, width=50)  # Fixed Width to width
        self.msg_entry.pack()
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()
        
        # Network Setup
        self.connect_to_server()  # Added missing connection call
        
        receive_thread = threading.Thread(target=self.receive_messages)  # Fixed method name
        receive_thread.daemon = True
        receive_thread.start()
    
    def connect_to_server(self):
        try:
            self.client_socket.connect(('localhost', 5555))
            self.display_message("[SYSTEM] Connected to server!")
        except Exception as e:
            self.display_message(f"[SYSTEM] Connection error: {str(e)}")
    
    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            try:
                self.client_socket.send(msg.encode('utf-8'))
                self.display_message(f"[YOU] {msg}")  # Added space for formatting
                self.msg_entry.delete(0, tk.END)
            except Exception as e:
                self.display_message(f"[SYSTEM] Error sending message: {str(e)}")
    
    def receive_messages(self):  # Fixed method name to match thread target
        while True:
            try:
                msg = self.client_socket.recv(1024).decode('utf-8')
                if msg:
                    self.display_message(f"[SERVER] {msg}")  # Added space for formatting
            except:
                self.display_message("[SYSTEM] Connection lost!")
                break
    
    def display_message(self, msg):
        self.chat_list.insert(tk.END, msg)
        self.chat_list.yview(tk.END)

root = tk.Tk()  # Fixed TK to Tk
app = ChatApp(root)
root.mainloop()