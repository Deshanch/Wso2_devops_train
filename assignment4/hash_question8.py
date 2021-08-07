import hashlib
import sys
import uuid # this is a standard library

#salt = b'Km5d5ivMy8iexuHcZrsD'
"""
A module from the standard library to generate secure random numbers. collisions happening us super small: one in 2^128
"""
salt = uuid.uuid4().bytes # get byte representation of the secure random number
password = sys.argv[1].encode('utf-8') # Convert the password to bytes
"""
key = hashlib.pbkdf2_hmac(
    'sha512', # The hash digest algorithm for HMAC
    password, 
    salt, # Provide the salt
    200000 # It is recommended to use at least 100,000 iterations of SHA-256 
)
"""
key = hashlib.sha512(salt + password).hexdigest()

print(key) # result gives the hex values, see what are those
#print(key.hex()) # this will print the hex values getting
