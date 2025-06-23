from website import create_app
from dotenv import load_dotenv
import os
from flask import Flask

# Load environment variables from .env file
load_dotenv()

app = create_app()

# Add a ping endpoint
@app.route('/ping')
def ping():
    return 'pong', 200

# Print the current SQLALCHEMY_DATABASE_URI for debugging
print('SQLALCHEMY_DATABASE_URI:', app.config.get('SQLALCHEMY_DATABASE_URI'))

if __name__ == '__main__':
    # Use environment variables for host and port
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host=host, port=port, debug=debug)