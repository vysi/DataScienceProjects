import time

# issues = ["issue 1", "issue 2", "issue 3"]
issues = []
for i in range(3):
    issues.append(f'issue {i+1}')

# print(issues)
# log = open("log.txt", "a")
# for i in issues:
#     s = f"time: {time.time()}\nerror: {i}\n"
#     log.write(s)
#
# log.close()

# Ohne issue Liste
# log = open("log2.txt", "a")
# for i in range(3):
#     s = f"time: {time.time()}\nerror: issue {i + 1}\n"
#     log.write(s)
#
# log.close()

def readError(eintrag):
    log = open('log.txt')
    entries = log.readlines()
    entry_tuple = []
    for i in range(0, len(entries)-1, 2):
        entry_tuple.append((entries[i], entries[i+1]))

    return entry_tuple[eintrag-1]

# Lies bestimmte zeile aus
# print(readError(2))
log = open('log.txt')
x = int(input('Zeile: '))
log.seek(0)
str = log.readlines()[x]

log.seek(0)
for i in range(x+1):
    line = log.readline()

log.close()
print(str)
print(line)
