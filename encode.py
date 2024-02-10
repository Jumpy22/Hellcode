original_string = "https://raw.githubusercontent.com/Jumpy22/Hellcode/main/b64msgbox64.bin"
bytes_list = [ord(char) for char in original_string]

# Convert bytes back to string
decoded_string = ''.join(chr(byte) for byte in bytes_list)

# Print the results
print("Original String:", original_string)
print("Bytes List:", bytes_list)
print("Decoded String:", decoded_string)
