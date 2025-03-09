```python
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
```
**sys:** Стандартная библиотека Python, используется для работы с системными функциями, например, для завершения программы.
**PySide6.QtWidgets:** Модуль библиотеки **PySide6**, который предоставляет классы для создания графического интерфейса (GUI).

**QApplication:** Главный класс, который управляет приложением (создаёт цикл событий и обрабатывает взаимодействие с пользователем).

**QMainWindow:** Класс для создания главного окна приложения.
**QTreeView:** Виджет для отображения иерархических данных (например, дерева).
**QTextEdit:** Виджет для отображения и редактирования текста.
**QVBoxLayout:** Менеджер компоновки, который располагает виджеты вертикально.
**QWidget:** Базовый класс для всех виджетов (окон, кнопок и т.д.).
**QLabel:** Виджет для отображения текста или изображений.

**Создание класса MainWindow**
```python
    class MainWindow(QMainWindow):    
```

**MainWindow:** Пользовательский класс, который наследуется от QMainWindow. Это главное окно приложения.

**Конструктор класса MainWindow**
```python
    def __init__(self):
    super().__init__()
```
__init__: Конструктор класса, который вызывается при создании объекта.
super().__init__(): Вызов конструктора родительского класса (QMainWindow), чтобы инициализировать главное окно.

**Настройка окна**
```python
    self.setWindowTitle("ST File Viewer")
    self.setGeometry(100, 100, 800, 600)
```

**setWindowTitle("ST File Viewer"):** Устанавливает заголовок окна.
**setGeometry(100, 100, 800, 600):** Устанавливает положение и размер окна:
**100, 100** — координаты верхнего левого угла окна на экране.
**800, 600** — ширина и высота окна.

**Создание главного виджета и layout**
```python
    main_widget = QWidget()
    main_layout = QVBoxLayout()
    main_widget.setLayout(main_layout)
    self.setCentralWidget(main_widget)
```
**QWidget():** Создаёт базовый виджет, который будет использоваться как контейнер для других виджетов.
**QVBoxLayout():** Создаёт вертикальный менеджер компоновки, который будет располагаться внутри main_widget.
**setLayout(main_layout):** Устанавливает QVBoxLayout для main_widget.
**setCentralWidget(main_widget):** Устанавливает main_widget как центральный виджет главного окна.

**Добавление заголовка для дерева**
```python
    tree_label = QLabel("Структура файла")
    main_layout.addWidget(tree_label)
```
**QLabel("Структура файла"):** Создаёт текстовую метку с текстом "Структура файла".
**addWidget(tree_label):** Добавляет метку в вертикальный layout (main_layout).

 **Создание QTreeView**
 ```python
    self.tree_view = QTreeView()
    self.tree_view.setHeaderHidden(True)
    main_layout.addWidget(self.tree_view)
 ```
**QTreeView():** Создаёт виджет для отображения иерархических данных (например, дерева).
**setHeaderHidden(True):** Скрывает заголовок дерева (если он есть).
**addWidget(self.tree_view):** Добавляет дерево в вертикальный layout.

**Добавление заголовка для текстового поля**
 ```python
    text_label = QLabel("Содержимое элемента")
    main_layout.addWidget(text_label)
 ```
**QLabel("Содержимое элемента"):** Создаёт текстовую метку с текстом "Содержимое элемента".
**addWidget(text_label):** Добавляет метку в вертикальный layout.

**Создание QTextEdit**
```python
    self.text_edit = QTextEdit()
    self.text_edit.setReadOnly(True)
    main_layout.addWidget(self.text_edit)
```
**QTextEdit():** Создаёт текстовое поле для отображения и редактирования текста.
**setReadOnly(True):** Делает текстовое поле доступным только для чтения (пользователь не сможет редактировать текст).
**addWidget(self.text_edit):** Добавляет текстовое поле в вертикальный layout.

**Запуск приложения**
```python
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
```
**QApplication(sys.argv):** Создаёт объект приложения. sys.argv передаёт аргументы командной строки.
**MainWindow():** Создаёт объект главного окна.
**window.show():** Отображает главное окно.
**app.exec_():** Запускает цикл событий приложения.
**sys.exit():** Завершает программу после закрытия окна.

**Итог:**

**Классы:**
**QApplication:** Управляет приложением.
**QMainWindow:** Главное окно приложения.
**QTreeView:** Виджет для отображения дерева.
**QTextEdit:** Виджет для отображения текста.
**QVBoxLayout:** Менеджер компоновки для вертикального расположения виджетов.
**QWidget:** Базовый виджет.
**QLabel:** Виджет для отображения текста.

**Методы:**
**setWindowTitle():** Устанавливает заголовок окна.
**setGeometry():** Устанавливает положение и размер окна.
**setLayout():** Устанавливает менеджер компоновки для виджета.
**setCentralWidget():** Устанавливает центральный виджет для главного окна.
**addWidget():** Добавляет виджет в layout.
**setHeaderHidden():** Скрывает заголовок дерева.
**setReadOnly():** Делает текстовое поле доступным только для чтения.


