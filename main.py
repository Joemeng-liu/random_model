"""by lmj"""
from model_list import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start:")
    name = 0
    while 1:
        key = input()
        # g start
        if key == 'g':
            name = model.load_model(name, model_list)
        # t stop
        if key == 't':
            break
    print("end")