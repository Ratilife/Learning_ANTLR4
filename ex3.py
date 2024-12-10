import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QTextDocument
from ex4 import PythonSyntaxHighlighter

app = QApplication(sys.argv)

# Создаем текстовый редактор
editor = QTextEdit()
editor.setPlainText("def hello():\n    print('Hello, World!') # This is a comment")

# Создаем подсветку синтаксиса
document = editor.document()
highlighter = PythonSyntaxHighlighter(document)

# Показываем редактор
editor.show()
sys.exit(app.exec_())
