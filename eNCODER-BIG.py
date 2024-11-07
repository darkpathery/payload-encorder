import argparse
import base64
import urllib.parse
import binascii
import quopri
from cryptography.fernet import Fernet

# ANSI escape codes for text color
RED_COLOR = "\033[1;31m"
YELLOW_COLOR = "\033[1;33m"
GREEN_COLOR = "\033[1;32m"
RESET_COLOR = "\033[0m"

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt the payload
def encrypt_payload(payload, key):
    cipher = Fernet(key)
    encrypted_payload = cipher.encrypt(payload.encode())
    return encrypted_payload

# Base64 encoding
def base64_encode(payload):
    encoded_payload = base64.b64encode(payload.encode()).decode('utf-8')
    return encoded_payload

# Hexadecimal encoding
def hex_encode(payload):
    encoded_payload = payload.encode().hex()
    return encoded_payload

# URL encoding
def url_encode(payload):
    encoded_payload = urllib.parse.quote(payload)
    return encoded_payload

# ASCII85 encoding
def ascii85_encode(payload):
    encoded_payload = base64.a85encode(payload.encode()).decode('utf-8')
    return encoded_payload

# Rot13 encoding
def rot13_encode(payload):
    encoded_payload = payload.encode('rot_13')  # Rot13 is normally used on text strings directly
    return encoded_payload

# Binary encoding
def binary_encode(payload):
    encoded_payload = ''.join(format(ord(char), '08b') for char in payload)
    return encoded_payload

# UUEncoding
def uuencode(payload):
    encoded_payload = binascii.b2a_uu(payload.encode()).decode('utf-8')
    return encoded_payload

# HTML Entity encoding
def html_entity_encode(payload):
    encoded_payload = ''.join(f"&#{ord(char)};" for char in payload)
    return encoded_payload

# Quoted-Printable Encoding
def quoted_printable_encode(payload):
    encoded_payload = quopri.encodestring(payload.encode()).decode('utf-8')
    return encoded_payload

# Dictionary of encoders
ENCODERS = {
    "Base64": base64_encode,
    "Hexadecimal": hex_encode,
    "URL": url_encode,
    "ASCII85": ascii85_encode,
    "Rot13": rot13_encode,
    "Binary": binary_encode,
    "UUEncode": uuencode,
    "HTML Entity": html_entity_encode,
    "Quoted-Printable": quoted_printable_encode
}

# Custom encoding function with encryption and multiple encoding methods
def custom_encode(payload, encoding_order):
    # Generate encryption key
    key = generate_key()
    # Encrypt payload
    encrypted_payload = encrypt_payload(payload, key)
    
    # Apply selected encodings in order
    for encoding_method in encoding_order:
        encoder_function = ENCODERS.get(encoding_method)
        if encoder_function:
            encrypted_payload = encoder_function(encrypted_payload.decode('utf-8') if isinstance(encrypted_payload, bytes) else encrypted_payload)
        else:
            print(f"Invalid encoding method: {encoding_method}")
            return None, None

    # Combine encrypted payload and key into a single string (step 2 + 3)
    combined_payload = f"{encrypted_payload}::{key.decode('utf-8')}"
    
    return combined_payload

# Function to retrieve the encoding order
def get_encoding_order(num_encodings):
    encoding_order = []
    for i in range(num_encodings):
        print(f"Available encoding methods: {', '.join(ENCODERS.keys())}")
        encoding_method = input(f"Enter encoding method #{i+1}: ")
        encoding_order.append(encoding_method)
    return encoding_order

if __name__ == "__main__":
    # Display ASCII art (you can add your own ASCII art here)
    print("eNCODER")

    # Ask the user to input the payload directly
    payload = input("Enter the payload to encode and encrypt: ")

    # Ask for the number of encoding steps
    num_encodings = int(input("How many encoding steps do you want to apply? "))

    # Get the encoding order
    encoding_order = get_encoding_order(num_encodings)

    # Process the payload with selected encoding order
    combined_payload = custom_encode(payload, encoding_order)

    if combined_payload:
        # Display the encoded payload and embedded key
        print(f"\nFINAL ENCODED PAYLOAD WITH EMBEDDED KEY: {combined_payload}")
