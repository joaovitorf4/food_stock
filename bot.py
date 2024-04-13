from time import sleep
import keyboard
from diet import Diet
from food import Food


my_diet = Diet()

my_diet.add_food(Food('Pasta de Amendoim', 1000, 20, 'g'))
my_diet.add_food(Food('Requeijão', 400, 60, 'g'))
my_diet.add_food(Food('Tapioca', 500, 90, 'g'))
my_diet.add_food(Food('Leite Desnatado', 6000, 800, 'L'))
my_diet.add_food(Food('Leite Integral', 4000, 400, 'L'))
my_diet.add_food(Food('Torrada', 54, 6, 'g'))
my_diet.add_food(Food('Ricota', 700, 60, 'g'))
my_diet.add_food(Food('Peito de Frango', 2000, 100, 'g'))
my_diet.add_food(Food('Pao Integral', 540, 120, 'g'))
my_diet.add_food(Food('Batata doce', 200, 150, 'g'))
my_diet.add_food(Food('Aveia', 500, 50, 'g'))
my_diet.add_food(Food('Banana', 20, 3, 'u'))
my_diet.add_food(Food('Granola', 900, 105, 'g'))

my_diet.start_timer()

print('This code is about to send a email of a Food Stock report')
print('Type the Key (E) any time you want to update the quantity in stock!')
print()

while True:
    keyboard.wait('e')
    my_diet.update_food()
    sleep(1)
