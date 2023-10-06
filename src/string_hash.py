import hashlib

def string_hash(input_string):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the input string encoded as bytes
    sha256_hash.update(input_string.encode('utf-8'))
    # Return the hexadecimal representation of the hash digest
    return sha256_hash.hexdigest()

# Example usage
# input_string = "Hello, World!"
# hashed_string = string_hash(input_string)