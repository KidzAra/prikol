x = float(input("Введите первое число: "))
while True:   
    try:
           user_choice = input("Что вы хотите сделать? (1 — калькулятор, 2 — выход, 3 — Очистить значение): ")
           match user_choice:
            case "1": print("Калькулятор")
            case "2":
                print("Выход")
                break
            case "3":
                print("Очистить")
                x = float(input("Введите первое число: "))
            case _:
                print("Неизвестная команда")
                break   
           y = float(input("Введите второе число: "))
           operator = input("Введите оператор (+, -, *, /): ")
           x = eval(f"{x}{operator}{y}")
           print("Результат:", x)
    except ZeroDivisionError:
       print("Делить на ноль нельзя")
    except ValueError:
       print("Это точно число?")
    except SyntaxError:
       print("Садись, ДВА!")
    except Exception as e:
       print(e)