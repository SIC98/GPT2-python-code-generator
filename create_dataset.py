from subprocess import call
import pickle
import random
import math
import os

with open('top100_repository.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    call(['git', 'clone', line.strip(), f'resources/{line.strip().split("/")[-1]}'])

total_data = []
total_files = []
count = 0

for line in lines:
    for currentpath, folders, files in os.walk(f'resources/{line.strip().split("/")[-1]}'):
        for file in files:
            if file[-3:] == '.py':
                count += 1
                total_files.append(os.path.join(currentpath, file))

print('files: ', len(total_files))

for file in total_files:
    with open(file, "r") as f:
        try:
            t = f.readlines()
        except UnicodeDecodeError:
            print('DecoderError: ', file)
        summary = ''.join(t)
        summary = str(summary).strip()
        bos_token = '<BOS>'
        eos_token = '<EOS>'
        data = bos_token + ' ' + summary + ' ' + eos_token
        total_data.append(data)

random.shuffle(total_data)
train_len = math.ceil(len(total_data) * 0.9)

with open("data/data.txt", "w") as fp:
    fp.write('\n'.join(total_data))

with open("data/train.txt", "w") as fp:
    fp.write('\n'.join(total_data[:train_len]))

with open("data/test.txt", "w") as fp:
    fp.write('\n'.join(total_data[train_len:]))
