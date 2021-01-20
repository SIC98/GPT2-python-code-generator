from subprocess import call
import math
import os
import csv
csv_columns = ['text']

with open('top100_repository.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    call(['git', 'clone', line.strip(), f'resources/{line.strip().split("/")[-1]}'])

json_data = []
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
        data = bos_token + summary + eos_token
        json_data.append({'text': data})

train_len = math.ceil(len(json_data) * 0.9)

with open("data/data.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in json_data:
            writer.writerow(data)

with open("data/train.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in json_data[:train_len]:
        writer.writerow(data)

    with open("data/test.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in json_data[train_len:]:
            writer.writerow(data)
