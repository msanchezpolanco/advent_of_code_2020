from sys import stdin, stdout

passwords = [x.strip() for x in stdin.readlines()]

valid = 0

# --- Part One ---
#for line in passwords:
#    length, letter, password = line.split()
#    min_length, max_length = length.split('-')
#
#    if password.count(letter[0]) >= int(min_length) and password.count(letter[0]) <= int(max_length):
#        valid += 1
#stdout.write(str(valid))

# --- Part Two ---
for line in passwords:
    length, letter, password = line.split()
    min_length, max_length = length.split('-')

    if bool(letter[0] == password[int(min_length)-1]) ^ bool(letter[0] == password[int(max_length)-1]):
        valid += 1
stdout.write(str(valid))
