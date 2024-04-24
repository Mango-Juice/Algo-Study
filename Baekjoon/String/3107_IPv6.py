raw = input().split(":")
answer = []
if not raw[0]: del raw[0]
if not raw[-1]: del raw[-1]

for i, s in enumerate(raw):
    length = len(s)
    if length == 0:
        answer.extend(["0000"] * (8 - len(raw) + 1))
    else:
        answer.append("0" * (4 - length)+ s)

print(":".join(answer))