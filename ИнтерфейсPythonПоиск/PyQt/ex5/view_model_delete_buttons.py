from typing import Dict, List
from PySide6.QtCore import QObject, Signal

class DeleteButtonsViewModel(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    # Сигнал для уведомления View об изменении данных
    buttonsUpdated = Signal()

    def get_buttons(self) -> List[Dict[str, str]]:
        """
        Возвращает список кнопок.
        """
        return self._model.get_buttons()

    def set_selected(self, name: str, selected: bool):
        """
        Устанавливает отметку для кнопки.
        """
        self._model.set_selected(name, selected)
        self.buttonsUpdated.emit()

    def get_selected_buttons(self) -> List[str]:
        """
        Возвращает список имен кнопок, которые были отмечены для удаления.
        """
        return self._model.get_selected_buttons()