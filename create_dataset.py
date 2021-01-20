from subprocess import call
import pickle
import random
import math
import json
import os

with open('top100_repository.txt', 'r') as f:
    lines = f.readlines()

# for line in lines:
#     call(['git', 'clone', line.strip(), f'resources/{line.strip().split("/")[-1]}'])

json_data = {}
total_files = []
count = 0

for line in lines:
    for currentpath, folders, files in os.walk(f'resources/{line.strip().split("/")[-1]}'):
        for file in files:
            if file[-3:] == '.py':
                count += 1
                total_files.append(os.path.join(currentpath, file))

print('files: ', len(total_files))

idx = 0
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
        data = bos_token + summary + eos_token
        json_data[idx] = data
        idx += 1

keys = list(json_data.keys())
random.shuffle(keys)

train_len = math.ceil(len(keys) * 0.9)

train_dict = {k: json_data[k] for k in keys[:train_len]}
test_dict = {k: json_data[k] for k in keys[train_len:]}

with open("data/data.json", "w") as fp:
    json.dump(json_data, fp, indent=4)

with open("data/train.json", "w") as fp:
    json.dump(train_dict, fp, indent=4)

with open("data/test.json", "w") as fp:
    json.dump(test_dict, fp, indent=4)
