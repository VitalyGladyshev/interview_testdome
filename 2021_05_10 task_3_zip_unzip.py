# Задача 3 +

import sys
import os
from zipfile import ZipFile

# def main(argv=None):
archive_path = sys.argv[1] if sys.argv is not None else sys.argv[1]

full_path = os.path.join(os.getcwd(), archive_path)
# print(full_path)

res_file = ""
file_src = ""

if os.path.exists(os.getcwd()):
    with ZipFile(full_path, "r") as zp_f:
        for file_in in zp_f.infolist():
            # print(file_in.filename)
            res_file = file_in.filename
            zp_f.extract(res_file)

with open(res_file) as r_file:
    file_src = r_file.read()

op_list = []
op_1 = ''
for el in file_src.split("\n"):
    if el[-1].isdigit():
        num_1 = 0
        for i in range(len(el)):
            num_1 += int(el[-(i+1)]) * 10 ** i
        # print(num_1)
        op_list.append(num_1)
    else:
        op_1 = el[-1]
        # print(f"оп: {el[-1]}")

res_val = None
if op_1 == "+":
    res_val = op_list[0]+op_list[1]
    # print(f"{op_list[0]} {op_1} {op_list[1]} = {op_list[0]+op_list[1]}")

elif op_1 == "-":
    res_val = op_list[0] - op_list[1]
    # print(f"{op_list[0]} {op_1} {op_list[1]} = {op_list[0] - op_list[1]}")

with open(res_file, 'a') as w_file:
    # print(f"res_val = {res_val}")
    w_file.write("\n"+str(res_val))

with ZipFile(full_path, "w") as zp_w:
    zp_w.write(res_file)