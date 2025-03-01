from dataclasses import dataclass
from typing import List

@dataclass
class ButtonModel:
    '''
    Это dataclass, который представляет собой модель данных для кнопки. Он содержит два поля: 
    name (название кнопки) и path (путь к программе, которую нужно запустить).
    '''
    name: str  # Название кнопки
    path: str  # Путь к программе

class ButtonListModel:
    '''
    Этот класс управляет списком кнопок. Он предоставляет методы для добавления новой кнопки (add_button), 
    получения списка всех кнопок (get_buttons) и получения конкретной кнопки по индексу (get_button).
    '''
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
    
    def remove_button(self, index: int):
        if 0 <= index < len(self._buttons):
            self._buttons.pop(index)

    def edit_button(self, index: int, name: str, path: str):
        if 0 <= index < len(self._buttons):
            self._buttons[index].name = name
            self._buttons[index].path = path        

    def is_valid_button(self, name: str, path: str) -> bool:
        return bool(name.strip()) and os.path.exists(path)        
    
    def sort_buttons(self, key=lambda button: button.name):
        self._buttons.sort(key=key)