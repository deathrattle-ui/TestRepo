import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests  # Import the requests library to fetch the public IP

# Set the directory where you want to save the uploaded files
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_public_ip():
    """Fetch the public IP address of the host machine."""
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Determine the size of data to read
        content_length = int(self.headers['Content-Length'])
        
        # Read the uploaded file data
        file_data = self.rfile.read(content_length)
        
        # Extract the filename from the request headers
        filename = self.headers['Filename'] if 'Filename' in self.headers else 'uploaded_file'
        filepath = os.path.join(UPLOAD_DIR, filename)
        
        # Save the uploaded file
        with open(filepath, 'wb') as output_file:
            output_file.write(file_data)
        
        # Send response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully')

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'HTTP server is running.')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    # Fetch the public IP address
    public_ip = "93.93.112.55"
    if not public_ip:
        print("Could not retrieve public IP. Exiting.")
        return

    # Prompt the user for a port number
    while True:
        try:
            port_input = input("Enter the port number to listen on (default: 14500): ")
            if not port_input:  # Use default if no input
                port = 14500
            else:
                port = int(port_input)
            
            if 0 <= port <= 65535:
                break
            else:
                print("Invalid port number. Please enter a number between 0 and 65535.")
        except ValueError:
            print("Please enter a valid integer for the port number.")
    
    # Bind the server to the local IP address or 0.0.0.0
    server_address = ('0.0.0.0', port)  # Listen on all interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on {public_ip}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
