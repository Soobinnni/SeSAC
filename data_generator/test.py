import math

max_size = 3
cur_page_num = 5
x = cur_page_num // max_size

start_index = max_size * (x + (1 / max_size))
end_index = max_size * (x + 1)

print(f"start:{start_index}, end : {end_index}")