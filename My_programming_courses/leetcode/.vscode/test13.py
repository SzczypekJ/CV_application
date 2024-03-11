def create_square_frame(n):
    frame = []

    if n <= 1:
        frame.append('*')
        return frame

    # Top line
    frame.append('*' * n)

    # Middle lines
    for _ in range(n - 2):
        frame.append('*' + ' ' * (n - 2) + '*')

    # Bottom line
    frame.append('*' * n)

    return frame


# Example usage:
n = 8
frame = create_square_frame(n)
for line in frame:
    print(line)
