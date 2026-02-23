def calculate_binary(x):
    if x == 0:
        return "0"
    binary = ""
    while x > 0:
        binary = str(x % 2) + binary
        x //= 2
    return binary

def main():
    print(calculate_binary(5))
    print(calculate_binary(255))
    print(calculate_binary(1))
    print(calculate_binary(0))
    
if __name__ == "__main__":
    main()