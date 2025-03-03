# Create a function that accepts a list of sandwich ingredients.
# The function should have one parameter that can collect as many arguments as the function call provides.
# The function should print a summary of the sandwich being ordered.
# Call the function two times with a different number of arguments.

def make_sandwich(*ingredients):
        print(f'I am making a sandwich with:') 
        for ingredient in ingredients:
             print(f'-{ingredient}')

make_sandwich('pepperoni', 'mayo', 'tomato')
make_sandwich('chicken', 'lettuce', 'humus', 'pickle', 'mayo')
make_sandwich('egg')
