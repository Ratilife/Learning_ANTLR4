import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QTextEdit, QSplitter, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QFile, QIODevice, QTextStream
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

        # Создаем QTreeView для отображения структуры
        self.tree_view = QTreeView()
        self.tree_view.setHeaderHidden(True)
        self.tree_view.clicked.connect(self.on_tree_item_clicked)  # Обработка клика по элементу
        main_layout.addWidget(self.tree_view)

        # Добавляем заголовок для текстового поля
        text_label = QLabel("Содержимое элемента")
        main_layout.addWidget(text_label)

        # Создаем QTextEdit для отображения содержимого
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        main_layout.addWidget(self.text_edit)

        # Загружаем данные из файла
        self.load_st_file("МоиШаблоны.st")

    def load_st_file(self, file_path):
        # Открываем файл и читаем его содержимое
        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            self.text_edit.setPlainText("Ошибка: Не удалось открыть файл.")
            return

        stream = QTextStream(file)
        content = stream.readAll()
        file.close()

        # Разбор структуры файла
        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)
        self.parse_st_content(content)

    def parse_st_content(self, content):
        try:
            # Ручной парсинг структуры файла
            data = self.parse_custom_format(content)
            self.build_tree(data, self.model.invisibleRootItem())
        except Exception as e:
            self.text_edit.setPlainText(f"Ошибка при разборе файла: {e}")

    def parse_custom_format(self, content):
        # Простейший ручной парсинг для примера
        # В реальном коде нужно реализовать более сложный парсер
        stack = []
        current = []
        buffer = ""
        i = 0
        while i < len(content):
            if content[i] == "{":
                stack.append(current)
                current = []
                i += 1
            elif content[i] == "}":
                if buffer.strip():
                    current.append(buffer.strip())
                    buffer = ""
                if stack:
                    last = stack.pop()
                    last.append(current)
                    current = last
                i += 1
            elif content[i] == ",":
                if buffer.strip():
                    current.append(buffer.strip())
                    buffer = ""
                i += 1
            else:
                buffer += content[i]
                i += 1
        return current[0] if current else []

    def build_tree(self, data, parent_item):
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list) and len(item) > 1:
                    # Извлекаем название элемента
                    name = item[1][0] if isinstance(item[1], list) else str(item[1])
                    new_item = QStandardItem(name)
                    parent_item.appendRow(new_item)

                    # Если есть вложенные элементы, рекурсивно их обрабатываем
                    if len(item) > 2:
                        self.build_tree(item[2:], new_item)

    def on_tree_item_clicked(self, index):
        # Обработка клика по элементу дерева
        item = self.model.itemFromIndex(index)
        self.text_edit.setPlainText(f"Выбран элемент: {item.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())