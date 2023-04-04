from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a new key
key = Fernet.generate_key()

# Instantiate a Fernet class
fernet = Fernet(key)

@app.route('/')
def home():
    return 'Welcome to the Cryptography App!'

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message'].encode()
    encrypted_message = fernet.encrypt(message)
    return {'encrypted_message': encrypted_message.decode()}

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message'].encode()
    decrypted_message = fernet.decrypt(encrypted_message)
    return {'decrypted_message': decrypted_message.decode()}

if __name__ == '__main__':
    app.run(debug=True)
