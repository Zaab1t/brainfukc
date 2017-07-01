def _trim_code(code):
    language = ['<', '>', '+', '-', '.', ',', '[', ']']
    return list(filter(lambda c: c in language, code))


def _create_loop_map(code):
    stack, loopmap = [], {}
    for i, char in enumerate(code):
        if char == '[': stack.append(i)
        if char == ']':
            start = stack.pop()
            loopmap[start] = i
            loopmap[i] = start
    return loopmap


def run(code, input_=None):
    """+[--------->++<]>.+++.-------.++[++>---<]>.--[->+++<]>.+++.-----
    --.[----->++<]>++.+[->++<]>+..+++++.+++++++++++.------------.----..
    ++++[->+++<]>.---------.---[->++++<]>.-----.[--->+<]>-----.---[----
    ->++<]>.-------------.----.+++.-[--->+<]>-.---[->++++<]>.----------
    --.+.++++++++++.+[---->+<]>+++.+[->+++<]>+.+++++++++++.------------
    .-[--->+<]>---.+.--.---------.+++++.-------.--[->+++<]>-.
    """
    tape, pointer, result, index = [0], 0, [], 0
    code = _trim_code(code)
    loopmap = _create_loop_map(code)

    if input_ is not None:
        input_iter = iter(input_)

    def next_input():
        if input_ is None:
            print('made it here')
            return ord(input())
        return ord(next(input_iter))
    
    while index < len(code):
        char = code[index]
        if char == '<':
            pointer -= 1
        elif char == '>':
            pointer += 1
            try:
                tape[pointer]
            except IndexError:
                tape.append(0)
        elif char == '+':
            tape[pointer] += 1 if tape[pointer] < 255 else -255
        elif char == '-':
            tape[pointer] -= 1 if tape[pointer] > 0 else -255
        elif char == '.':
            result.append(chr(tape[pointer]))
        elif char == ',':
            tape[pointer] = next_input()
        elif char == '[' and tape[pointer] == 0: index = loopmap[index]
        elif char == ']' and tape[pointer] != 0: index = loopmap[index]
        index += 1
                
    return ''.join(result)
