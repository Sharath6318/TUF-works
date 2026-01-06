def findvalid(v):

    valid_dict = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
    }

    stack = []
    
    for val in v:

        if val in valid_dict:

            stack.append(val)

        elif val in valid_dict.values():

            if not stack:

                return False
            
            last = stack.pop()

            if valid_dict[last] != val:

                return False
            
    return len(stack) == 0

print(findvalid("[())]"))  


























#     stack = []

#     for char in v:

#         if char in valid_dict:

#             stack.append(char) 

#         elif char in valid_dict.values():

#             if not stack:

#                 return False
            
#             last = stack.pop() 

#             if valid_dict[last] != char:

#                 return False

#     return len(stack) == 0

# print(findvalid("[()]"))


            



