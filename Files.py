# Simple example of writing data to a file
import io as io;

newFile = io.FileIO("test_file.txt", mode="w")

textToWrite = "This is some text"

# newFile.write( textToWrite )

textRange = range( len(textToWrite) - 1, 0, -1)

for t in textToWrite:
    newFile.write(t + '\n')


for t in textRange:
    newFile.write(textToWrite[t])

newFile.close()


# Very simple file viewer
import glob as glob
import io
filename = raw_input('Enter a filename: ')
matches = glob.glob(filename)
if matches:
    file = io.FileIO(matches[0])
    print(file.read())
else:
    print('No matches')
