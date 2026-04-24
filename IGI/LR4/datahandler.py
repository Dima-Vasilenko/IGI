class DataHandler:
    @staticmethod
    def get_int(prompt):
        """Recieve int value"""
        while True:
            try:
                value = int(input(prompt))
                if (value <= 0):
                    continue
                return value
            except ValueError:
                print("Ошибка! Введите число: ")

    @staticmethod
    def get_float(prompt):
        """Recieve float value"""
        while True:
            try:
                value = float(input(prompt))
                # if (value <= 0):
                #     continue
                return value
            except ValueError:
                print("Ошибка! Введите число: ")


