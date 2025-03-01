from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QHBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QByteArray, QBuffer, QIODevice, QSize
from model import ButtonListModel
from view_model import ButtonViewModel
import base64
import sys

class MainWindow(QMainWindow):
    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model
        self.setWindowTitle("Панель кнопок")

        # Основной виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Основной layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Панель для кнопок
        self.buttons_layout = QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)

        # Кнопка для добавления новой кнопки с иконкой
        self.add_button = QPushButton()
        icon = self.load_icon_from_base64(add_icon)
        if icon.isNull():
            print("Ошибка: Иконка не загружена!")
        else:
            self.add_button.setIcon(icon)
            # Устанавливаем размер кнопки по размеру иконки
            icon_size = icon.pixmap(icon.availableSizes()[0]).size()
            self.add_button.setFixedSize(icon_size)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.buttons_layout.addWidget(self.add_button)

        # Кнопка "Закрыть панель"
        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close_panel)
        self.buttons_layout.addWidget(self.close_button)

        # Инициализация кнопок
        self.update_buttons()

        # Подписка на изменение списка кнопок
        self.view_model.buttonsChanged.connect(self.update_buttons)

    def add_button_clicked(self):
        # Диалог для добавления новой кнопки
        name, ok1 = QInputDialog.getText(self, "Добавить кнопку", "Введите название:")
        path, ok2 = QInputDialog.getText(self, "Добавить кнопку", "Введите путь к программе:")
        if ok1 and ok2:
            self.view_model.add_button(name, path)

    def close_panel(self):
        # Закрытие приложения
        self.close()

    def update_buttons(self):
        # Очистка текущих кнопок
        for i in reversed(range(self.buttons_layout.count())):
            widget = self.buttons_layout.itemAt(i).widget()
            if widget != self.add_button and widget != self.close_button:
                widget.setParent(None)

        # Добавление новых кнопок справа от кнопки "Добавить" и "Закрыть"
        buttons = self.view_model.get_buttons()
        for i, button in enumerate(buttons):
            btn = QPushButton(button.name)
            btn.clicked.connect(lambda checked, idx=i: self.view_model.execute_program(idx))
            self.buttons_layout.addWidget(btn)

    def load_icon_from_base64(self, base64_data: str) -> QIcon:
        # Декодирование base64 и создание QIcon
        icon_data = base64.b64decode(base64_data)
        pixmap = QPixmap()
        pixmap.loadFromData(icon_data)
        if pixmap.isNull():
            print("Ошибка: Не удалось загрузить изображение из base64!")
        return QIcon(pixmap)

# Иконка в формате base64
add_icon = b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAACVklEQVR4nO1ZvW4TQRBeQaCgJFDx8xIRUVK5Q5F20MwVJxD0vAIojbuEPkROxBsY3YzkAA0FzwCCB4CkIj91jgY0Z8cSVpD3btd3e+g+aSVLJ9vfNzuz+82cMR06dPBGOkyvAtO6FdwEwcwyfQOmMxD8VSymM8v0tXgmuPkoS9b6/f4V0zRQ8B4wvQKmIxD6XW7hoRXc3siSu7UT3ximt0Fo3wrm5Yn/vaxgbgUHMIJbtZAHwacgeOpL/BIhJzZLniyM+Mr+82uW6U1o4jArhGlP/ysoeRjBDSv4YdHk4WIxvdf/DBf5OsnLVMTHdJhe9xZQR9rAv+ti4Ec+S541RR6mCx9XIk9My5bpOAIBp5WOWD3nmydP41Ri2i1FXm9H30tqFp61kMMI7rtHX+2BZ9RCCoCxiG0n8mqy1KfEJgCYjtQ0ukR/PUTeBhcgRS2szhUwtsRxCgCmly47wBELeDt/B4rGI1oBX+bvQAmrHArgXgPHLjWQxyoAmM7/fwHQ+hTithcxt/0YlXgvMiv4Yq4AHTrFKgCy5IGTmbNMP2ITYJm+O0/z1LrGJgAEt0xbGxpgOrcH9o6zgMkuDILkbZCFO6YsHg7TmzE09VbwpPLcVGeVjQvgJK1EfiqCaa/B6L82vtA+1DJJA3n/rvept2RCQAetxcC1vsgfBBvuzgx5B3WkTS9U5C+DzioXczrhT++CLTk33dULxps462/gjh7bpm7o7ai2o4p3Gn8Ht0rfsIvAxACu6txGPbs2HtrZTV7g5cVnps/6TC2xusooXrN26GDajz+jYGvHi7pQwQAAAABJRU5ErkJggg=='

if __name__ == "__main__":
    app = QApplication([])

    # Создаем Model
    model = ButtonListModel()

    # Создаем ViewModel и передаем ей Model
    view_model = ButtonViewModel(model)

    # Создаем View и передаем ему ViewModel
    window = MainWindow(view_model)
    window.show()

    sys.exit(app.exec())