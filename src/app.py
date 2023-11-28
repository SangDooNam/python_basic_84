#!/usr/bin/env python
from typing import Union, Callable


def compare_to_seven(input: Union[int, str, Callable]) -> str:
    
    # TODO: write function
    if isinstance(input, int):
        if input > 7:
            return f'{input} is higher than 7.'
        elif input == 7:
            return f"{input} is 7."
        else:
            return f'{input} is lower than 7.'
    elif isinstance(input, str) and input.isnumeric():
        if  int(input) > 7:
            return f'{input} is higher than 7.'
        elif int(input) == 7:
            return f"{input} is 7."
        else:
            return f'{input} is lower than 7.'
    elif isinstance(input, str) and not input.isnumeric():
        try:
            if ord(input) > 7:
                return f'{input} is higher than 7.'
            elif ord(input) == 7:
                return f"{input} is 7."
            else:
                return f'{input} is lower than 7.'
        except TypeError:
            if len(input) > 7:
                return f'{input} is higher than 7.'
            elif len(input) == 7:
                return f"{input} is 7."
            else:
                return f'{input} is lower than 7.'
    elif isinstance(input, Callable):
        return 'It is callable'
    
    
    
if __name__ == "__main__":
    compare_to_seven(8)
