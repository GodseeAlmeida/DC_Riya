import threading
import time
import random

class Clock:
    def __init__(self):
        self.time = 0
        self.lock = threading.Lock()

    def get_time(self):
        with self.lock:
            return self.time

    def set_time(self, new_time):
        with self.lock:
            self.time = new_time

class Node(threading.Thread):
    def __init__(self, node_id, clock):
        super().__init__()
        self.node_id = node_id
        self.clock = clock

    def run(self):
        iterations = 10  # Set the number of iterations
        for _ in range(iterations):
            # Simulate some computation
            self.do_some_work()

            # Update the clock
            with self.clock.lock:
                current_clock = self.clock.time + 1
                self.clock.time = current_clock

            # Print the clock of this node
            print("Node", self.node_id, "- Clock:", current_clock)

            # Sleep for some time before repeating
            time.sleep(1)

    def do_some_work(self):
        # Simulate some computation
        time.sleep(random.random())

def main():
    # Create a clock instance
    clock = Clock()

    # Create and start multiple nodes
    for i in range(2):
        node = Node(i, clock)
        node.start()

if __name__ == "__main__":
    main()
