def to_binary(position, height):
    # Convert position to binary path
    binary = bin(position).zfill(height)

    return binary


position = 2
height = 10
print(to_binary(position, height))
