<h1>Simple Chat Application</h1>

<p>This repository contains a basic client-server chat application built with Python. It demonstrates fundamental concepts of network programming using sockets and multithreading to handle multiple client connections.</p>
<img width="1916" height="1019" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/04f9e591-0ce7-465c-a379-e244debdc1a5" />


<h2>Features</h2>
<ul>
  <li>Multi-client support: The server can handle connections from multiple clients concurrently.</li>
  <li>Basic messaging: Clients can send messages to the server, and the server can respond.</li>
  <li>Connection handling: Graceful handling of client disconnections.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<p>You need Python 3.x installed on your system.</p>

<h3>Installation</h3>
<p>1. Clone this repository:</p>
<pre><code>git clone https://github.com/nimranoor99/Chat-App/</code></pre>
<p>2. Navigate to the project directory:</p>
<pre><code>cd simple-chat-app</code></pre>

<h3>Usage</h3>

<h4>1. Start the Server</h4>
<p>Open a terminal and run the server script:</p>
<pre><code>python chat_server.py</code></pre>
<p>The server will start listening for incoming connections.</p>

<h4>2. Start the Client(s)</h4>
<p>Open one or more separate terminals and run the client script:</p>
<pre><code>python gui_chat.py</code></pre>
<p>or if you have a CLI client:</p>
<pre><code>python cli_chat.py</code></pre>
<p>Each client will attempt to connect to the server. Once connected, you can type messages and send them.</p>

<h2>Files</h2>
<ul>
  <li><code>chat_server.py</code>: The Python script for the chat server.</li>
  <li><code>gui_chat.py</code>: The Python script for the GUI-based chat client.</li>
  <li><code>cli_chat.py</code> (<em>if applicable, based on screenshot</em>): The Python script for a command-line interface chat client.</li>
</ul>

<h2>How it Works (Briefly)</h2>
<ul>
  <li>The <code>chat_server.py</code> creates a socket, binds it to a specific address and port, and listens for incoming connections.</li>
  <li>When a client connects, the server spawns a new thread (using the <code>threading</code> module) to handle that client's communication independently.</li>
  <li>Each client thread receives messages from its respective client and can send responses back.</li>
  <li>The <code>gui_chat.py</code> (or <code>cli_chat.py</code>) connects to the server and provides an interface for sending and receiving messages.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this repository and contribute. Any improvements or new features are welcome!</p>

<h2>License</h2>
<p>This project is open source and available for everyone to copy and add additional features in it.</p>

</body>
</html>
