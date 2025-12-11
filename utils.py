def read_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f'Please enter a value >= {min_value}')
                continue
            if max_value is not None and value > max_value:
                print(f'Please enter a value <= {max_value}')
                continue
            return value
        except ValueError:
            print('Please enter a valid integer.')

def read_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('Input cannot be empty.')

def pause():
    input('\nPress Enter to continue...')