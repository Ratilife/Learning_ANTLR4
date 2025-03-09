import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QTextEdit, QSplitter, QVBoxLayout, QWidget
from PyQt5.QtCore import QFile, QIODevice, QTextStream

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ST File Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Создаем QTreeView для отображения структуры
        self.tree_view = QTreeView()
        self.tree_view.setHeaderHidden(True)

        # Создаем QTextEdit для отображения содержимого
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # Создаем QSplitter для разделения окна на две части
        splitter = QSplitter()
        splitter.addWidget(self.tree_view)
        splitter.addWidget(self.text_edit)

        # Устанавливаем QSplitter как центральный виджет
        self.setCentralWidget(splitter)

        # Загружаем данные из файла
        self.load_st_file("МоиШаблоны.st")

    def load_st_file(self, file_path):
        # Открываем файл и читаем его содержимое
        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return

        stream = QTextStream(file)
        content = stream.readAll()
        file.close()

        # Здесь будет логика для разбора структуры файла и заполнения tree_view
        # Пока просто выведем содержимое в text_edit
        self.text_edit.setPlainText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())