from typing import List, Dict

class DeleteButtonsModel:
    def __init__(self, buttons: List[Dict[str, str]]):
        self._buttons = buttons  # Список кнопок с именами и путями
        self._selected_buttons = {button["name"]: False for button in buttons}  # Словарь для хранения отметок

    def get_buttons(self) -> List[Dict[str, str]]:
        """
        Возвращает список кнопок.
        """
        return self._buttons

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