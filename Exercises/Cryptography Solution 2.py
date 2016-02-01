import io
from Crypto.Cipher import Blowfish

# We'll want to do this more than once so define a function
def showMenu():
    choice = int(raw_input("Choose: \n 1: Encrypt a message\n 2: Decrypt a message\n 3: Exit\n"))
    return choice

choice = showMenu()

# Loop round until the user chooses something other than 1 or 2
while (choice == 1 or choice == 2):
    if choice == 1:
        key = raw_input("Enter a key :\n")
        message = raw_input("Enter a message: \n")
        # We need to ensure the total plaintext length is a multiple of 8 for this cipher
        bfish = Blowfish.new( key, Blowfish.MODE_ECB)
        msglen = len(message)
        # A simple modulo check. We'll pad until it passes
        while (msglen % 8) is not 0:
            message += 'X'
            msglen = len(message)

        ciphertext = bfish.encrypt(message)
        print(ciphertext)
        export = raw_input("Export to file? (y/n)")
        if ( export.lower() == 'y' ):
            filename = raw_input('Filename : ')
            outfile = io.FileIO( filename, 'w+')
            outfile.write( ciphertext )
            # Don't forget to close the file when we're done
            outfile.close()
    elif choice == 2:
        filename = raw_input('Filename : ')
        infile = io.FileIO( filename, 'r+')
        ciphertext = infile.read()
        key = raw_input('Key : \n')
        bfish = Blowfish.new( key, Blowfish.MODE_ECB)
        plaintext = bfish.decrypt(ciphertext)
        print(plaintext)
        # Don't forget to close the file when we're done
        infile.close()
    # Get the menu choice again for the loop
    choice = showMenu()
