from PySide6.QtCore import QObject, Signal

class ButtonViewModel(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model  # Ссылка на Model

    # Сигнал для уведомления View об изменении данных
    buttonsChanged = Signal()

    def add_button(self, name: str, path: str):
        # Добавление новой кнопки через Model
        self._model.add_button(name, path)
        self.buttonsChanged.emit()  # Уведомление View об изменении

    def get_buttons(self):
        # Получение списка кнопок через Model
        return self._model.get_buttons()

    def execute_program(self, index: int):
        # Запуск программы через Model
        button = self._model.get_button(index)
        if button:
            import os
            os.startfile(button.path)  # Запуск программы