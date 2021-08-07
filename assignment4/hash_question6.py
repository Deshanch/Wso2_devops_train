import hashlib
import sys

salt = b'Km5d5ivMy8iexuHcZrsD'
password = sys.argv[1].encode('utf-8') # Convert the password to bytes

key = hashlib.pbkdf2_hmac(
    'sha512', # The hash digest algorithm for HMAC
    password, 
    salt, # Provide the salt
    200000 # It is recommended to use at least 100,000 iterations of SHA-256 
)

#print(key) # result gives the hex values, see what are those
print(key.hex()) # this will print the hex values getting
