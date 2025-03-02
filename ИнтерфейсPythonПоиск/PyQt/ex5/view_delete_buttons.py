from typing import List
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt

class DeleteButtonsDialog(QDialog):
    def __init__(self, view_model, parent=None):
        super().__init__(parent)
        self.view_model = view_model
        self.setWindowTitle("Удаление кнопок")
        self.setModal(True)

        # Основной layout
        layout = QVBoxLayout(self)

        # Таблица для отображения кнопок
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Имя кнопки", "Удалить"])
        self.table.setRowCount(len(self.view_model.get_buttons()))

        # Заполнение таблицы
        for i, button in enumerate(self.view_model.get_buttons()):
            name_item = QTableWidgetItem(button["name"])
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  # Запрещаем редактирование
            self.table.setItem(i, 0, name_item)

            checkbox = QCheckBox()
            checkbox.stateChanged.connect(lambda state, name=button["name"]: self.view_model.set_selected(name, state == Qt.Checked))
            self.table.setCellWidget(i, 1, checkbox)

        layout.addWidget(self.table)

        # Кнопки "ОК" и "Отмена"
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def get_selected_buttons(self) -> List[str]:
        """
        Возвращает список имен кнопок, которые были отмечены для удаления.
        """
        return self.view_model.get_selected_buttons()