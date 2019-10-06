from stack import Stack

def match_brackets(symbol_str):
    symbol_pairs = {
        '(': ")",
        '{': "}",
        '[': "]"
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        # extracting each symbol from the symbol string
        symbol =  symbol_str[index]

        # Push onto stack when you find opening braces
        if symbol in openers:
            my_stack.push(symbol)
        else:
            # When a closing brace comes

            # when the stack is empty, there's no matching brace
            if my_stack.is_empty():
                return False
            else:
                # checking if there is a matching brace on the stack
                top = my_stack.pop()
                if(symbol != symbol_pairs[top]):
                    return False
        # iterating to the next index
        index += 1
    # when all the elements are parsed, check if the stack is empty
    if(my_stack.is_empty()):
        return True
    
    return False

if(__name__ == "__main__"):
    print(match_brackets('([{}])'))
    print(match_brackets('(([()])'))