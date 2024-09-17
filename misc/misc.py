import time
from dataclasses import dataclass
import random

@dataclass
class Example():
    x: int 
    y: int

if __name__ == "__main__":
    examples = [Example(0,0)] *1000 + [Example(0,1)] *1000 + [Example(1,0)] *1000 + [Example(1,1)] *1000 + [Example(2,2)] *1000
    random.shuffle(examples)

    t0 = time.time()
    for example in examples:
        if isinstance(example, Example):
            if example.x==0 and example.y==0:
                z=1
            # elif example.x==0 and example.y==1:
            #     z=11
            # elif example.x==1 and example.y==0:
            #     z=12
            # elif example.x==1 and example.y==1:
            #     z=13
            # else:
            #     z=0
    print(time.time()-t0)
    
    t1 = time.time()
    for example in examples:
        match example:
            case Example(x=0, y=0):
                z=1
            # case Example(x=0, y=1):
            #     z=11
            # case Example(x=1, y=0):
            #     z=12
            # case Example(x=1, y=1):
            #     z=13
            # case _:
            #     z=0
    print(time.time()-t1)
