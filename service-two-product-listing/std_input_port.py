import controller as controller
import sys

if __name__ == "__main__":
    """
    Reads the lines coming from the stdin and send them to controller
    """
    data = sys.stdin.readlines()
    for event in data:
        print(controller.receive(event))