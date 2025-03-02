from typing import List, Dict
from model import ButtonListModel  # Предполагается, что ButtonListModel определен в модуле model

class DeleteButtonsModel:
    def __init__(self, model: ButtonListModel):
        self._model = model  # Ссылка на ButtonListModel
        # тут ошибка
        self._selected_buttons = {button.name: False for button in self._model.get_buttons()}  # Словарь для хранения отметок

    def set_selected(self, name: str, selected: bool):
        """
        Устанавливает отметку для кнопки.
        """
        if name in self._selected_buttons:
            self._selected_buttons[name] = selected

    def get_selected_buttons(self) -> List[str]:
        """
        Возвращает список имен кнопок, которые были отмечены для удаления.
        """
        return [name for name, selected in self._selected_buttons.items() if selected]