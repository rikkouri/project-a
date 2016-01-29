import threading, time
# Define the function that will do the work
# We're passing in the flag so the calling code can listen to it
def sleeper(flag):
    print('Running')
    print('Sleeping')
    # Make the thread wait for 10 seconds
    time.sleep( 10 )
    print('Waking')
    time.sleep(1)
    # Signal calling code that we're done
    flag.set()

# Create the Event object we're going to listen to
event = threading.Event()
# Create the thread, specifying the function we defined as the target and providing a
# tuple for the arguments. Note the trailing comma in the tuple
thread = threading.Thread(group=None, target=sleeper, name=None, args=(event,))
thread.start()
# Wait for the flag to get set before continuing with the program
event.wait()
print('Stopping')