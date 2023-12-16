# main.py
from AI import run_AI
from DataProcessing import *
from GUI import *
from SSS import *

import asyncio

async def main():
    
    # Create tasks for each module
    task_SSS = asyncio.create_task(run_SSS())
    task_AI = asyncio.create_task(run_AI())
    task_Data_Processing = asyncio.create_task(run_Data_Processing())

    # Wait for all tasks to complete
    await asyncio.gather(task_SSS, task_AI, task_Data_Processing)

# Run the event loop
asyncio.run(main())
