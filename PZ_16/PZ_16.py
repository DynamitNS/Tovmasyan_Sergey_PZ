# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.
class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self, step=1):
        """Увеличивает значение счетчика на заданный шаг (по умолчанию на 1)"""
        self.value += step

    def decrement(self, step=1):
        """Уменьшает значение счетчика на заданный шаг (по умолчанию на 1)"""
        self.value -= step

    def get_value(self):
        """Возвращает текущее значение счетчика"""
        return self.value

    def reset(self):
        """Сбрасывает счетчик в ноль"""
        self.value = 0
counter = Counter(5)
print(f"Начальное значение: {counter.get_value()}")
counter.increment()
print(f"После инкремента: {counter.get_value()}")
counter.increment(3)
print(f"После инкремента на 3: {counter.get_value()}")
counter.decrement(2)
print(f"После декремента на 2: {counter.get_value()}")
counter.reset()
print(f"После сброса: {counter.get_value()}")
