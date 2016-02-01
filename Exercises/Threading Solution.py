import threading, thread, time

# Define the function that will do the thread work
def threadMain(name, interval):
    count = 0
    while count < 5:
        time.sleep(interval)
        count += 1
        print( name + " : count : " + str(count) + " " + time.ctime() + '\n' )
    return

try:
    print('Started at ' + time.ctime())
    # Create the threads and hold a reference to them
    threadOne = threading.Thread(target=threadMain, args=( 'Thread-1', 2, ) )
    threadTwo = threading.Thread(target=threadMain, args=( 'Thread-2', 4, ) )
    threadOne.start()
    threadTwo.start()
    print(threadOne.name + " started")
    print(threadTwo.name + " started")
except:
    print('Error starting thread')

# Loop until both threads have finished, i.e. return False for isAlive()
while threadOne.isAlive() or threadTwo.isAlive():
    pass

print('Done')
exit()

