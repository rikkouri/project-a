from Crypto.Cipher import Blowfish

key = raw_input("Enter a key :\n")
message = raw_input("Enter a message: \n")

bfish = Blowfish.new( key, Blowfish.MODE_ECB)
msglen = len(message)
while (msglen % 8) is not 0:
    message += 'X'
    msglen = len(message)

ciphertext = bfish.encrypt(message)
print(ciphertext)

plaintext = bfish.decrypt(ciphertext)
print(plaintext)
