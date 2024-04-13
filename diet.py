import threading
from time import sleep
from email_sender import EmailSender
from get_time import get_current_time
from html_builder import HTMLBuilder

DAY_IN_SECONDS = 60 * 60 * 24

class Diet:
    def __init__(self):
        self._items = []
        self._timer_thread = threading.Thread(
            target=self._update_quantities_thread, daemon=True)
        self._email_sender = EmailSender()

    def start_timer(self):
        self._timer_thread.start()

    def add_food(self, food):
        self._items.append(food)

    def remove_food(self, food):
        self._items.remove(food)

    def update_food(self):
        print("Digite o nome da comida:")
        food_name = input()
        print("Digite a quantidade a ser atualizada:")
        new_qtd = int(input())
        for food in self._items:
            if food.name == food_name:
                food.qtd = new_qtd
                print("Food updated: Sucess!")
                return True
        print("Food not updated: Failure!")
        return False

    def generate_html(self):
        html_builder = HTMLBuilder(self._items)
        return html_builder.build_html()

    def _update_quantities_thread(self):
        while True:
            self._update_quantities()
            output = self.generate_html()
            self._email_sender.send_email("Diet Update", output)
            print(get_current_time() + " - Email sent!")
            sleep(DAY_IN_SECONDS)

    def _update_quantities(self):
        for food in self._items:
            food.qtd -= food.portion
            if food.qtd < 0:
                food.qtd = 0
            food.time_to_end = food.qtd // food.portion
