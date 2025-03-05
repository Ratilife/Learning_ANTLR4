import os
import json
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
    def __init__(self, file_path: str = "buttons.json"):
        self._buttons: List[ButtonModel] = []  # Список кнопок
        self._file_path = file_path
        self.load_buttons()  # Загружаем кнопки при инициализации
    def is_button_name_unique(self, name: str) -> bool:
        return not any(button.name == name for button in self._buttons)
    
    def add_button(self, name: str, path: str):
        # Добавление новой кнопки
        if self.is_button_name_unique(name):
            self._buttons.append(ButtonModel(name, path))
        #if self.is_valid_button(name, path) and self.is_button_name_unique(name):
        #    self._buttons.append(ButtonModel(name, path))
        else:
            raise ValueError("Кнопка с таким именем уже существует или данные невалидны.")

    def get_buttons(self) -> List[ButtonModel]:
        # Получение списка кнопок
        return self._buttons

    def get_button(self, index: int) -> ButtonModel:
        # Получение кнопки по индексу
        if 0 <= index < len(self._buttons):
            return self._buttons[index]
        return None
    def remove_button_list(self):
        #Удалить кнопки указанные в списке
        pass

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

    def save_buttons(self):
        """
        Сохраняет кнопки в файл в формате JSON.
        """
        data = [{"name": button.name, "path": button.path} for button in self._buttons]
        with open(self._file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_buttons(self):
        """
        Загружает кнопки из файла JSON.
        """
        if not os.path.exists(self._file_path):
            return  # Файл не существует, пропускаем загрузку

        with open(self._file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                self.add_button(item["name"], item["path"])