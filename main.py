# Zhafira Elham 1/21

import os
# import config

def get_words(file_path):
    with open(file_path, 'r') as f:
        # print(f.readlines())
        text = f.readlines()[0]
        #print(text.split())
        words = text.split()
    return words

def send_message(direct, message):
    os.system('osascript send.scpt {} "{}"'.format(direct, message))
    # testing line = os.system('osascript send.scpt 08xxxxxxxx "Move to main.py rather than terminal test1"')


if __name__ == '__main__':
    words = get_words('test.txt')
    receipent = 'random.email@gmail.com'
    for word in words:
        send_message(receipent, word)
