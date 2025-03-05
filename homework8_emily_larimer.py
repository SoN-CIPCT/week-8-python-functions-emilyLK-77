def make_sandwich(*ingredients):
        print(f'I am making a sandwich with:') 
        for ingredient in ingredients:
             print(f'-{ingredient}')

make_sandwich('pepperoni', 'mayo', 'tomato')
make_sandwich('chicken', 'lettuce', 'humus', 'pickle', 'mayo')
make_sandwich('egg')