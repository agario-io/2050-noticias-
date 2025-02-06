from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# Log visitor IPs
def log_visitor(ip):
    try:
        with open("visitor_logs.txt", "a") as f:
            f.write(f"{datetime.now()} - {ip}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

@app.route('/')
def index():
    # Log the visitor's IP
    visitor_ip = request.remote_addr
    log_visitor(visitor_ip)
    
    # Render the main page
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the logs file exists
    if not os.path.exists("visitor_logs.txt"):
        open("visitor_logs.txt", "w").close()
    app.run(host='0.0.0.0', port=10000)
