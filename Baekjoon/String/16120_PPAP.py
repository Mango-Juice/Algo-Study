inp = input()
stack = []

for c in inp:
    stack.append(c)
    while len(stack) >= 4 and stack[-4:] == ["P", "P", "A", "P"]:
        del stack[-4:]
        stack.append("P")

print("PPAP" if stack == ["P"] else "NP")