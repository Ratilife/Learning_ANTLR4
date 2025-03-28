from dataclasses import dataclass
from typing import List

@dataclass
class ButtonModel:
    name: str  # Название кнопки
    path: str  # Путь к программе

class ButtonListModel:
    def __init__(self):
        self._buttons: List[ButtonModel] = []  # Список кнопок

    def add_button(self, name: str, path: str):
        # Добавление новой кнопки
        self._buttons.append(ButtonModel(name, path))

    def get_buttons(self) -> List[ButtonModel]:
        # Получение списка кнопок
        return self._buttons

    def get_button(self, index: int) -> ButtonModel:
        # Получение кнопки по индексу
        if 0 <= index < len(self._buttons):
            return self._buttons[index]
        return None