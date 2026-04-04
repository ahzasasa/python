# match: takes an expression and compares its value to successive patterns given as one or more case blocks.
# If no case matches, none of the branches is executed.


# Compares a subject value against one or more literals:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
        
# Combine iterals:

case 401 | 403 | 404:
    return "Not allowed"


# Bind variable:

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")