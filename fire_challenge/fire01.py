
import sys
import re


OPERAND = ['*', '/', '%', '-', '+']

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    def analyse(exp):
        return exp.split(' ')

    def calculate(exp_a, ope, exp_b):
        if ope == '+':
            return float(exp_a) + float(exp_b)
        elif ope == '-':
            return float(exp_a) - float(exp_b)
        elif ope == '/':
            return float(exp_a) / float(exp_b)
        elif ope == '*':
            return float(exp_a) * float(exp_b)
        elif ope == '%':
            return float(exp_a) % float(exp_b)

    def run_parenthesis(exp):
        exp_solve = None
        parenthesis_tbl = re.findall('\((.*)\)', exp)
        if len(parenthesis_tbl) > 0:
            for pt in range(len(parenthesis_tbl)):
                par_solve = run_exp(analyse(parenthesis_tbl[pt]))
                exp_solve = exp.replace(re.findall('\(.*\)', exp)[pt], str(par_solve[0]))

        return exp_solve if exp_solve is not None else exp

    def run_ope(values, ope):
        solve = values
        while ope in solve:
            for j in range(len(solve)):
                if j + 1 < len(solve) - 1 and solve[j + 1] == ope:
                    tmp = calculate(solve[j], solve[j + 1], solve[j + 2])
                    for i in range(3):
                        del solve[j]
                    solve.insert(j, tmp)
                    break

        return solve

    def run_exp(values):
        tmp_values = values
        for op in OPERAND:
            tmp_values = run_ope(tmp_values, op)
            if len(tmp_values) < 2:
                return tmp_values

        return tmp_values

    try:
        args[0] = run_parenthesis(args[0])
        clean_args = analyse(args[0])
        resolve = run_exp(clean_args)
        print(resolve)

    except ValueError as ve:
        print('Error.')
