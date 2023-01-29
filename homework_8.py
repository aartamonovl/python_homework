expr_str = ' 2    1+(( 1 0- 5 ) ** 3 ) * ( 2+3    )+ ( 4 * ( 2   0 - 20 /        ( 5 - 1 ))) * ( 2^2 + 7 )'


def format_expr(expr):
    '''Обработка выражения для дальнейшего рассчета. Удаление лишних пробелов, добавление недостающих.'''
    expr = " ".join(expr.split())
    form_expr = ''
    for item in expr:
        if item.isalpha():
            print('В выражении присутствует недопустимый символ {}'.format(item))
            exit()
        if len(form_expr) == 0:
            form_expr = item
        else:
            if (item.isdigit() and form_expr[-1].isdigit()) or item == ' ':
                form_expr += item
            elif item.isdigit() and form_expr[-2].isdigit():
                form_expr = form_expr[:-1] + item
            elif item == '*' and form_expr[-1] == '*':
                form_expr += item
            else:
                if form_expr[-1] != ' ':
                    form_expr += ' ' + item
                else:
                    form_expr += item
    return form_expr


def str_expr_calc(expr_str: str) -> None:
    '''Парсер сложных выражений. Допустимые операции: +, -, *, /, **, ^'''

    oper_dict = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                 '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
                 '^': (3, lambda x, y: x**y), '**': (3, lambda x, y: x**y)}

    num_stack = []
    oper_stack = []

    expr_list = expr_str.split()

    for item in expr_list:
        if item.isdigit():
            num_stack.append(int(item))
        elif item in oper_dict:
            if len(oper_stack) == 0:
                oper_stack.append(item)
                continue
            if oper_stack[-1] == '(':
                oper_stack.append(item)
                continue

            while oper_stack:
                if oper_dict.get(item)[0] <= oper_dict.get(oper_stack[-1])[0]:
                    y, x = num_stack.pop(), num_stack.pop()
                    num_stack.append(oper_dict[oper_stack[-1]][1](x, y))
                    del oper_stack[-1]
                oper_stack.append(item)
                break

        elif item == ')':
            while oper_stack[-1] != '(':
                y, x = num_stack.pop(), num_stack.pop()
                num_stack.append(oper_dict[oper_stack[-1]][1](x, y))
                del oper_stack[-1]
            del oper_stack[-1]
        else:
            oper_stack.append(item)

    while len(oper_stack) > 0:
        y, x = num_stack.pop(), num_stack.pop()
        num_stack.append(oper_dict[oper_stack[-1]][1](x, y))
        del oper_stack[-1]

    result = num_stack.pop()

    print(expr_str + ' = ' + str(result))


str_expr_calc(format_expr(expr_str))
