class Food:
    def __init__(self, name, qtd, portion, tipo_arm):
        self.name = name
        self.qtd = qtd
        self.portion = portion
        self.tipo_arm = tipo_arm
        self.time_to_end = qtd // portion
