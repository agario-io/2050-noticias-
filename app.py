from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Log visitor IPs
def log_visitor(ip):
    with open("visitor_logs.txt", "a") as f:
        f.write(f"{datetime.now()} - {ip}\n")

@app.route('/')
def index():
    # Log the visitor's IP
    visitor_ip = request.remote_addr
    log_visitor(visitor_ip)
    
    # Render the main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)