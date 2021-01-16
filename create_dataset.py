from subprocess import call

with open('top100_repository.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    call(['git', 'clone', line.strip(), f'resources/{line.strip().split("/")[-1]}'])
