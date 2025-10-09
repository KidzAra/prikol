phase = int(0)
cm = int(0)

while cm != 10:
    catCommand = input()

    if catCommand == "пошел с тапка":
        if phase == 0:
            print("Кот открывает один глаз и игнорирует вас")
            phase += 1
        elif phase == 1:
            print("Кот дергает хвостом")
            phase += 1
        elif phase == 2:
            print("кот ворчит")
            phase += 1
        elif phase >= 3:
            print("кот сдвинулся на 1 сантиметр")
            cm += 1
    
    if cm >= 10:
        print("кот убежал")
        break
            