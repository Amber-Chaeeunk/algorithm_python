def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))