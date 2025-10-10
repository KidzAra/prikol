zombies = int(100)
ammo = int(200)
distance = float(8)
global kills
kills = int(0)

def zombieShootout(zombies, ammo, distance):
    while zombies > 0:
        global kills
        if distance <= 0:
            print("зомби добрались до вас. Вы погибли. вы убили " + str(kills) + " зомби")
            return
        if ammo > 0:
            print("Вы выстрелили в зомби")
            ammo -= 1
            distance -= 0.5
            zombies -= 1
            kills += 1
            print("осталось зомби: " + str(zombies))
            print("осталось патронов: " + str(ammo))
            print("расстояние до зомби: " + str(distance))
        else:
            print("у вас кончились патроны. Вы погибли. вы убили " + str(kills) + " зомби")
            return
    
    print("Вы убили всех зомби. Вы выжили! Вы убили " + str(kills) + " зомби")
    return


zombieShootout(zombies, ammo, distance)