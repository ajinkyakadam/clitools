"""
Implementing tail cli tool in python
"""

import argparse
import time
from queue import Queue

def tail_lines(filepath, n=10):
    """
    returns the last n lines of the file
    """
    q = Queue()
    maxlines = 0

    with open(filepath, 'r') as f:
        for line in f:
            q.put(line)
            if maxlines >= n:
                q.get()
            else:
                maxlines +=1
    
    for line in range(maxlines):
        data = q.get()
        print(data.rstrip('\n'))

def tail_follow(filepath):

    try:
        with open(filepath, 'r') as f:
            f.seek(0,2) # go to the end
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(1)
                    f.seek(where)
                else:
                    print(line.rstrip('\n'))
    except KeyboardInterrupt:
        print("Keyboard interrupt received")
        pass
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple implementation of tail cli tool in python")

    parser.add_argument(
        'filepath',
        type=str,
        help="file absolute path that should be tailed" 
    )
    parser.add_argument(
        '-n',
        '--num',
        dest='lines',
        type=int,
        help="number of lines to be tailed"
    )
    parser.add_argument(
        '-f',
        '--follow', 
        dest='follow',
        default=False,
        action='store_true',
        help="follow the file continuously"
    )


    args = parser.parse_args()

    if args.lines:
        tail_lines(args.filepath,args.lines)
    elif args.follow:
        tail_follow(args.filepath)
    else:
        tail_lines(args.filepath)