

import random
numbers = random.sample(range(1000,100000000), 100000)

with open("Output.txt", "w") as text_file:
    for number in numbers:
        hex_string = '{:02x}'.format(number)
        if len(hex_string)>7:
            continue
        text_file.write(hex_string+"\n")
