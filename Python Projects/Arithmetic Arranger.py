def arithmetic_arranger(problems, show=False):

    first = ""
    second = ""
    lines = ""
    sumx = ""
    output = ""
    solution = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        num1, op, num2 = problem.split()
        if op == "*" or op == "/":
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op == "+":
            solution = str(int(num1)+int(num2))
        if op == "-":
            solution = str(int(num1)-int(num2))
        
        max_len = max(len(num1), len(num2))
        top = str(num1).rjust(max_len+2)
        bottom = op + str(num2).rjust(max_len + 1)
        line = "-"*(max_len + 2)
        res = str(solution).rjust(max_len+2)

        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            sumx += res + "    "
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
        
    if show:
        output = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        output = first + "\n" + second + "\n" + lines

    return output