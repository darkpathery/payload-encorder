import argparse
import base64
from cryptography.fernet import Fernet

# Add your ASCII art here
ASCII_ART = "\033[1;31m" + r"""

                                            66 73 71  68



                                        :^^:            :^^:
                                      !B&##&G!       .?B&##&P:
                                      B@GB&?#@J7JYYJ!5@GJ&GB@Y
                                      !GBBY P@@B5YYP#@@?:PBBP^
                                        .  ~&&7     .Y@#.
                                           G@Y        B@J
                              .::^^^:.     B@?        P@5     .:^^^:..
                         .~JPB########B57: P@Y        B@? ^?PB#######BG5?^
                       ^Y#&GY7~:....:~?P&&55@B       :&@YG@#57^:...:^~75B&B?:
                     .Y@&J:             .7#@@&^      7@@@G!.             ^Y@&7
                     5@G.                 .J@@?      P@#7                  ^#@?
                    ~@&:        .^!7??!~:.  !P7      J5^  .^~7??7~:         !@&.
                    !@&:      !P#&BGPPGB##P7.          :JG##BGPPG#&BY^      !@&:
                     Y@#J~^~?B@G7..^~~^:^!5&&J       :5&#J~^:^~~:.:?#@G7^^!Y&&7
                      ^YGB#BBY~  7#&BB##BGPG@@P^:.:^~B@&PPGB##BB&G~  !5B##BG?:
                          ..    ^@@!  .:~7YG#@@@@&&@@@@#PJ7~:.  J@#.    ..
                                .P@BY5PGBBBG#@@G7!!?#@@BGBBBGPY5#@J
                                  ~JYJ7!~::Y&&5:    ~P&#?:^~7?YY?^
                                     ^!. :B@5:        ^B@5  ^!:
                                   !B@B~ B@Y           .G@Y ?#@P^
                                  7@&!  !@#.            ~@&:  ?@&^
                                  B@?   ?@G             :&@~   P@5
                                 .#@7   !@#:            ~@&:   5@P
                                  Y@P    G@Y            G@Y   :#@7
                                  .B@Y   ^&@?          5@G.  .G@5
                                   .B@B~  ^B@5:      ^G@P.  7#@5
                                  ~5&#5:   .Y&&Y^ .~P@#7    ~P&#J:
                                .G@B?.       :JB&B#&G7.       :J#@Y
                                 !~             ^!!:            .!~
""" + "\033[0m"

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

# Custom encoding function with encryption
def custom_encode(payload):
    # Generate encryption key
    key = generate_key()
    # Encrypt payload
    encrypted_payload = encrypt_payload(payload, key)
    # Convert encrypted payload to base64 for better obfuscation
    encoded_payload = base64.b64encode(encrypted_payload).decode('utf-8')
    return encoded_payload, key

if __name__ == "__main__":

# Display ASCII art
    print(ASCII_ART)

    parser = argparse.ArgumentParser(description='Encode and encrypt a payload')
    parser.add_argument('payload', type=str, help='The payload to encode and encrypt')
    args = parser.parse_args()

    encoded_payload, key = custom_encode(args.payload)

     # Display encoded payload in green inside brackets
    print("\nENCODED PAYLOAD:", f"[{GREEN_COLOR}{encoded_payload}{RESET_COLOR}]")
    
    # Display encryption key in yellow inside brackets
    print("ENCRYPTED KEY:", f"[{YELLOW_COLOR}{str(key)}{RESET_COLOR}]")


