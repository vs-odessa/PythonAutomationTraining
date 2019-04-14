def generate_fibonacci(length):
    if length <= 0:
        return []
    if length == 1:
        return [1]
    else:
        fib_list = [1, 1]
        i = len(fib_list)
        while i < length:
            next_value = fib_list[-1] + fib_list[-2]
            fib_list.append(next_value)
            i += 1
        return fib_list

if __name__ == "__main__":
    my_list = generate_fibonacci(10)
    print(*my_list)