
def load_sample(name):
    file_path = 'samples/' + name
    state = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            state.append([1 if c == '1' else 0 for c in line])
    return state
