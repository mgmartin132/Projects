# A CLI file validation tool

import time
import os
import hashlib

def file_hash(file_path):
    hasher = hashlib.sha256() # Function calculates the hash of a file using SHA256 algorithm
    with open(file_path, 'rb') as file: # Opens the file in binary mode
        for chunk in iter(lambda: file.read(4096), b""): # Reads the file in iterations of 4096 byte chunks
            hasher.update(chunk) # Updates the internal state of the hash algorithm for each chunk processed
    return hasher.hexdigest() # Returns the hexadecimal representation of the final hash digest
  
def file_compare(file_path1, file_path2):
    # Function compares the hash values of two files
    file_hash1 = file_hash(file_path1)
    file_hash2 = file_hash(file_path2)

    if file_hash1 == file_hash2:
        print("Hash match. The files are identical.")
    else:
        print("Hash mismatch. The files are different.")

# Reads user input of desired files for comparison
file_path1 = input("File 1 path: ")
file_path2 = input("File 2 path: ")

# Verifies the existence of specified files
if not os.path.exists(r"file_path1"):
    print(f"Error: Unable to locate '{file_path1}'")
    time.sleep(1)
    print("Exiting program.")
    time.sleep(1)
    quit()
if not os.path.exists(file_path2):
    print(f"Error: Unable to locate '{file_path2}'")
    time.sleep(1)
    print("Exiting program.")
    time.sleep(1)
    quit

# Calls the comparison function and stores the result
result = file_compare(file_path1, file_path2)
print(result)