#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/32/section/1

def draw_triangle(num_stars, base_length):
    if num_stars < 1:
        return
    else:
        # Print the stars, aligned to the center, with spaces before them
        print(f'{"*" * num_stars: ^19}'.rstrip())
        # Recursively call the function with num_stars reduced by 2 and base_length staying the same
        draw_triangle(num_stars - 2, base_length)

if __name__ == '__main__':
    base_length = int(input())  # Input for the base length of the triangle
    draw_triangle(base_length, base_length)
