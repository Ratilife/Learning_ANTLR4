from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QListView
from model import ButtonListModel
from view_model import ButtonViewModel
class MainWindow(QMainWindow):
    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model

        # Основной виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Список кнопок
        self.list_view = QListView()
        self.list_view.setModel(self.view_model)
        self.layout.addWidget(self.list_view)

        # Кнопка для добавления новой кнопки
        self.add_button = QPushButton("Добавить кнопку")
        self.add_button.clicked.connect(self.add_button_clicked)
        self.layout.addWidget(self.add_button)

        # Обработка нажатия на элемент списка
        self.list_view.doubleClicked.connect(self.item_double_clicked)

    def add_button_clicked(self):
        # Диалог для добавления новой кнопки
        name, ok1 = QInputDialog.getText(self, "Добавить кнопку", "Введите название:")
        path, ok2 = QInputDialog.getText(self, "Добавить кнопку", "Введите путь к программе:")
        if ok1 and ok2:
            self.view_model.add_button(name, path)

    def item_double_clicked(self, index):
        # Запуск программы при двойном клике на кнопку
        self.view_model.execute_program(index.row())

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