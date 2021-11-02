# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import uvicorn

#from core.logging import LOGGER

#logger = LOGGER.get_logger()


def start_app(name):
    # Use a breakpoint in the code line below to debug your script.
    #logger.info(f'Starting Application, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    uvicorn.run("restApi:app", host="127.0.0.1", port=8000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app(sys.path)
