def feet_to_steps (steps = float()):
    steps = steps * 2.5
    return int(steps) 

if __name__ == '__main__':
    steps = float(input())
    print(f"{feet_to_steps(steps)}")