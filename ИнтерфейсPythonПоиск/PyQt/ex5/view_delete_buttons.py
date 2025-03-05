# Модуль для диалогового окна удаления кнопок с использованием PySide6
from typing import List  # Импортируем List для аннотаций типов
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QCheckBox   # Импортируем необходимые классы для создания GUI
from PySide6.QtCore import Qt  # Импортируем Qt для использования констант

class DeleteButtonsDialog(QDialog):
    """
    Класс для диалогового окна, позволяющего пользователю выбирать кнопки для удаления.
    """
    def __init__(self, view_model, parent=None):
        """
        Инициализация диалогового окна.
        
        :param view_model: Модель представления, содержащая данные о кнопках.
        :param parent: Родительский виджет (по умолчанию None).
        """
        super().__init__(parent)                    # Вызов конструктора родительского класса
        self.view_model = view_model                # Сохранение ссылки на модель представления
        self.setWindowTitle("Удаление кнопок")      # Установка заголовка окна 
        self.setModal(True)                         # Установка окна как модального

        # Основной layout
        layout = QVBoxLayout(self)                  # Создание вертикального layout для размещения элементов

        # Таблица для отображения кнопок
        self.table = QTableWidget()                                         # Создание таблицы
        self.table.setColumnCount(2)                                        # Установка количества колонок
        self.table.setHorizontalHeaderLabels(["Имя кнопки", "Удалить"])     # Установка заголовков колонок
        self.table.setRowCount(len(self.view_model.get_buttons()))          # Установка количества строк в таблице

        # Заполнение таблицы
        for i, button in enumerate(self.view_model.get_buttons()):          # Перебор кнопок из модели представления
            name_item = QTableWidgetItem(button["name"])                    # Создание элемента таблицы для имени кнопки
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)      # Запрещаем редактирование имени кнопки
            self.table.setItem(i, 0, name_item)                             # Установка элемента в первую колонку
            # Подключение сигнала изменения состояния чекбокса к методу модели представления
            checkbox = QCheckBox()                                          # Создание чекбокса для выбора кнопки для удаления  
            checkbox.stateChanged.connect(lambda state, name=button["name"]: self.view_model.set_selected(name, state == Qt.Checked))  
            self.table.setCellWidget(i, 1, checkbox)                        # Установка чекбокса во вторую колонку

        layout.addWidget(self.table)

        # Кнопки "ОК" и "Отмена"
        button_layout = QHBoxLayout()                                       # Создание горизонтального layout для кнопок
        ok_button = QPushButton("OK")                                       # Создание кнопки "ОК"
        ok_button.clicked.connect(self.accept)                              # Подключение сигнала нажатия к методу принятия
        cancel_button = QPushButton("Отмена")                               # Создание кнопки "Отмена"
        cancel_button.clicked.connect(self.reject)                          # Подключение сигнала нажатия к методу отклонения                
        button_layout.addWidget(ok_button)                                  # Добавление кнопки "ОК" в layout
        button_layout.addWidget(cancel_button)                              # Добавление кнопки "Отмена" в layout
        layout.addLayout(button_layout)                                     # Добавление кнопок в основной layout

    # Изменить метод на удаление
    def get_selected_buttons(self) -> List[str]:
        """
        Возвращает список имен кнопок, которые были отмечены для удаления.

        :return: Список имен выбранных кнопок.
        """
        return self.view_model.get_selected_buttons()                       # Вызов метода модели представления для получения выбранных кнопок
    