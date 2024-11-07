# payload-encorder
A customizable payload encoder for obfuscating data using various encoding methods, enhancing security for diverse payloads. Future updates will include universally adaptable encoders, offering personalized obfuscation solutions tailored to individual security needs.

# eNCODER BIG

# Description

A customizable payload encoder designed for obfuscating data using multiple encoding techniques. This tool enhances security by allowing flexible encoding methods for a wide range of payload types. Currently, a future update is planned to create universally adaptable encoders for individual users, offering personalized obfuscation solutions.

# Features

Custom Encoding: Encodes payloads using both encryption and Base64 encoding for added obfuscation.
Encryption Key Generation: Automatically generates a random encryption key for each payload.
Enhanced Security: Ensures the payload is encrypted before being encoded, increasing security.
ANSI Color-Coded Output: Encoded payload and encryption key are displayed with color-coding for better readability.

# Technologies Used

Python: Main programming language.
Cryptography: Fernet encryption (from the cryptography library).
Base64: For encoding the encrypted payload.
Argparse: Command-line argument parsing.



# Installation

# 1. Clone the repository:
   
  git clone https://github.com/yourusername/eNCODER-BIG.git
    cd eNCODER-BIG

# 2. Install required dependencies:

    pip install cryptography

# Usage

 Run the program and pass a payload to encode:

 python encoder.py "YourPayloadHere"

 Example output

ENCODED PAYLOAD: [<color-coded encoded payload>]
ENCRYPTED KEY: [<color-coded encryption key>]

# Future Development
 Working on universally adaptable encoders for personalized obfuscation solutions.

