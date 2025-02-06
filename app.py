from flask import Flask, render_template, request
from datetime import datetime
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get PostgreSQL connection string from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Function to log visitor IPs
def log_visitor(ip):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Create logs table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS visitor_logs (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP NOT NULL,
                ip VARCHAR(50) NOT NULL
            );
        ''')

        # Insert the visitor's IP
        cur.execute('INSERT INTO visitor_logs (timestamp, ip) VALUES (%s, %s);',
                    (datetime.now(), ip))

        # Commit and close the connection
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error logging visitor: {e}")

@app.route('/')
def index():
    # Log the visitor's IP
    visitor_ip = request.remote_addr
    log_visitor(visitor_ip)

    # Render the main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    # Render the main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
