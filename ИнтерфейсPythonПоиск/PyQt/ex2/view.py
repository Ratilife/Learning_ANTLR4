from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QHBoxLayout
from model import ButtonListModel
from view_model import ButtonViewModel

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

        # Кнопка для добавления новой кнопки
        self.add_button = QPushButton("Добавить кнопку")
        self.add_button.clicked.connect(self.add_button_clicked)
        self.main_layout.addWidget(self.add_button)

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

    def update_buttons(self):
        # Очистка текущих кнопок
        for i in reversed(range(self.buttons_layout.count())):
            self.buttons_layout.itemAt(i).widget().setParent(None)

        # Добавление новых кнопок
        buttons = self.view_model.get_buttons()
        for i, button in enumerate(buttons):
            btn = QPushButton(button.name)
            btn.clicked.connect(lambda checked, idx=i: self.view_model.execute_program(idx))
            self.buttons_layout.addWidget(btn)

if __name__ == "__main__":
    app = QApplication([])

    # Создаем Model
    model = ButtonListModel()

    # Создаем ViewModel и передаем ей Model
    view_model = ButtonViewModel(model)

    # Создаем View и передаем ему ViewModel
    window = MainWindow(view_model)
    window.show()

    app.exec()