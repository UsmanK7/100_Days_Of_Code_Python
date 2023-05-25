# it is not recommended to modify a global variables
# but if you really want to then you can do it by two ways

# way-1
enemies = 2
def incease_enemies():
    global enemies
    enemies += 1
    return enemies
enemies = incease_enemies()
print(enemies)

# way-2
enemy2=3
def increase_enemy2():
    return enemy2+1
enemy2=increase_enemy2()
print(enemy2)
