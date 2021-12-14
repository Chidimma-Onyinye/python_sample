import time
import asyncio
import threading
"""
Synchronization of threading
"""

def timeout():
    print("1st timeout is started again")
    time.sleep(5)
    print("1st timeout is finished")

def timeout2():
    print("1st timeout is started")
    time.sleep(5)
    print("1st timeout is finished")

async def main():
    print("main is started")
    threading.Thread(target=timeout).start()
    threading.Thread(target=timeout2).start()
    print("Main is finished")