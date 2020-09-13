import re

s = '0110011'

while True:
    pattern = '10|01'
    new_s = re.sub(pattern, '', s)
    print(f"new_s : {new_s}, s:{s}")
    if new_s == s: break
    s = new_s

print(s)