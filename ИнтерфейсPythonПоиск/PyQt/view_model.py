from PySide6.QtCore import QAbstractListModel, Qt, Signal

class ButtonViewModel(QAbstractListModel):
    def __init__(self, model):
        super().__init__()
        self._model = model  # Ссылка на Model

    # Сигнал для уведомления View об изменении данных
    dataChanged = Signal()

    def rowCount(self, parent=None):
        return len(self._model.get_buttons())

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._model.get_buttons()[index.row()].name
        return None

    def add_button(self, name: str, path: str):
        # Добавление новой кнопки через Model
        self._model.add_button(name, path)
        self.dataChanged.emit()  # Уведомление View об изменении

    def execute_program(self, index: int):
        # Запуск программы через Model
        button = self._model.get_button(index)
        if button:
            import os
            os.startfile(button.path)  # Запуск программы