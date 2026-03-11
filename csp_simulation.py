import asyncio

"""
Communicating Sequential Processes (CSP):
The principle that "programs are composed of independent processes 
that communicate by passing messages over channels."

In modern AI:
This model is the basis for distributed training (PyTorch Distributed) 
and asynchronous inference pipelines.
"""

async def producer(channel):
    """A process that generates data and sends it through a channel."""
    for i in range(5):
        data = f"Token_{i}"
        print(f"Producer sending: {data}")
        await channel.put(data)
        await asyncio.sleep(0.5)
    await channel.put(None)  # Signal completion

async def consumer(channel):
    """A process that receives data from a channel and processes it."""
    while True:
        data = await channel.get()
        if data is None:
            break
        print(f"Consumer received: {data} -> Processing in GenAI pipeline...")
        await asyncio.sleep(1)

async def main():
    # The channel (queue) is the core of CSP communication
    channel = asyncio.Queue()
    
    print("Starting CSP simulation (Producer-Consumer message passing)...")
    
    # Run independent processes concurrently
    await asyncio.gather(
        producer(channel),
        consumer(channel)
    )
    print("All processes completed.")

if __name__ == "__main__":
    asyncio.run(main())
