import sys

lines_count = 0
my_bool = False
counter = 0
try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        if sys.argv[1][-3:] != ".py":
            print("Not a Python file")
            sys.exit(1)

    with open(file_name, "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

else:
    for line in lines:
        striped_line = line.strip()
        if not striped_line or striped_line.startswith("#"): # check empty line or comment
            continue
        if striped_line.startswith('"""') or striped_line.startswith("'''"): # check docstring
            counter += 1
            if counter == 2:
                my_bool = False
                counter = 0  # reset the counter when docstring is closed
            else:
                my_bool = True

        lines_count += 1

    print(lines_count)
    sys.exit(0)
