height = int(input())
max_chars = ((height - 1) * 2) + 1

i = 0
while i < height:
    num_of_chars = ""
    num_of_chars += "#"*(i*2)
    num_of_chars += "#"
    spaces_before = (max_chars - len(num_of_chars)) / 2
    current_line = (" " * int(spaces_before))
    current_line += num_of_chars
    print(current_line)
    i += 1

