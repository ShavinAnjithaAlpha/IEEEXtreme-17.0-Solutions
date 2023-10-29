mem = [0 for i in range(20)]
instruction_str = """
const/32 v0,<Input A>
const/32 v1,<Input B>
const/32 v2,<Input C>
const/32 v3,1
sub-int v4,v3,v3
sub-int v5,v4,v3
move v6,v3
move v7,v4
sub-int v7,v7,v1
move v8,v0
move v9,v0
add-int v9,v0,v1
move v10,v4
move v11,v4
move v12,v3
:l0
add-int v11,v11,v1
add-int v10,v10,v0
move v13,v10
move v14,v4
move v15,v4
:l1
add-int v16,v13,v13
if-le v16,v1,:l2
sub-int v13,v13,v1
add-int v14,v14,v3
add-int v15,v15,v1
goto :l1
:l2
if-gt v13,v4,:l3
sub-int v13,v4,v13
:l3
move v17,v4
move v18,v3
:l4
add-int v17,v17,v13
add-int v18,v18,v3
if-le v18,v6,:l4
move v18,v3
:l5
sub-int v17,v17,v9
add-int v18,v18,v3
if-le v18,v12,:l5
if-ge v17,v4,:l6
move v5,v14
move v6,v12
move v7,v15
move v8,v10
move v9,v13
:l6
add-int v12,v12,v3
if-le v12,v2,:l0
return v6
"""


def read(address):
    return mem[int(address[1:])]


def write(address, value):
    mem[int(address[1:])] = value


def sub(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rd, rs, rt) = rst.split(",")
    value = read(rs) - read(rt)
    write(rd, value)
    return pc + 1


def add(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rd, rs, rt) = rst.split(",")
    value = read(rs) + read(rt)
    write(rd, value)
    return pc + 1


def declare(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rd, value) = rst.split(",")
    write(rd, int(value))
    return pc + 1


def move(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rd, rs) = rst.split(",")
    write(rd, read(rs))
    return pc + 1


def jump(ins, pc):
    (opcode, label) = ins.split(" ")
    return jump_points[label]


def ifge(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rs, rt, label) = rst.split(",")
    if (read(rs) >= read(rt)):
        return jump_points[label]
    return pc + 1


def ifgt(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rs, rt, label) = rst.split(",")
    if (read(rs) > read(rt)):
        return jump_points[label]
    return pc + 1


def iflt(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rs, rt, label) = rst.split(",")
    if (read(rs) < read(rt)):
        return jump_points[label]
    return pc + 1


def ifle(ins, pc):
    (opcode, rst) = ins.split(" ")
    (rs, rt, label) = rst.split(",")
    if (read(rs) <= read(rt)):
        return jump_points[label]
    return pc + 1


def return_val(ins, pc):
    (opcode, rst) = ins.split(" ")
    return read(rst)


def ins_execute(ins_mem):
    pc = 0
    while (True):
        ins = ins_mem[pc]
        if (ins.startswith("const/32")):
            pc = declare(ins, pc)
        elif (ins.startswith("move")):
            pc = move(ins, pc)
        elif (ins.startswith("add-int")):
            pc = add(ins, pc)
        elif (ins.startswith("sub-int")):
            pc = sub(ins, pc)
        elif (ins.startswith("if-ge")):
            pc = ifge(ins, pc)
        elif (ins.startswith("if-le")):
            pc = ifle(ins, pc)
        elif (ins.startswith("if-gt")):
            pc = ifgt(ins, pc)
        elif (ins.startswith("if-lt")):
            pc = iflt(ins, pc)
        elif (ins.startswith("goto")):
            pc = jump(ins, pc)
        elif (ins.startswith("return")):
            value = return_val(ins, pc)
            print(value)
            break


def prepare_instuction(ins_split, jump_points):
    ins_mem = []
    i = 0
    for ins in ins_split:
        if not ins:
            continue
        if not ins[0] == ":":
            ins_mem.append(ins)
            i += 1
        else:
            jump_points[ins] = i

    return ins_mem


N = int(input())
for _ in range(N):
    (A, B, C) = input().split(" ")
    instruction_str_ = instruction_str.replace("<Input A>", A)
    instruction_str_ = instruction_str_.replace("<Input B>", B)
    instruction_str_ = instruction_str_.replace("<Input C>", C)

    ins_split = instruction_str_.split("\n")
    i = 0
    jump_points = {}
    ins_mem = prepare_instuction(ins_split, jump_points)
    ins_execute(ins_mem)
