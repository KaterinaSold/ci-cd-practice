import sys

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Только целые числа")
    if n < 0:
        raise ValueError("Не может быть отрицательным")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        print("Введите число для факториала:")
        user_input = input().strip()
        
        if user_input.lower() in ('q', 'exit', 'quit'):
            sys.exit(0)
            
        n = int(user_input)
        result = factorial(n)
        print(f"{n}! = {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except KeyboardInterrupt:
        print("\nВыход")
        sys.exit(0)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()