import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QTextEdit, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("ST File Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Создаем главный виджет и layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Добавляем заголовок для дерева
        tree_label = QLabel("Структура файла")
        main_layout.addWidget(tree_label)

        # Создаем QTreeView для отображения структуры (пока пустой)
        self.tree_view = QTreeView()
        self.tree_view.setHeaderHidden(True)
        main_layout.addWidget(self.tree_view)

        # Добавляем заголовок для текстового поля
        text_label = QLabel("Содержимое элемента")
        main_layout.addWidget(text_label)

        # Создаем QTextEdit для отображения содержимого (пока пустой)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        main_layout.addWidget(self.text_edit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())