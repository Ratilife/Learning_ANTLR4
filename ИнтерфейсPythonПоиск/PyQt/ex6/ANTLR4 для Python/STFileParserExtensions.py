# STFileParserExtensions.py
class STFileParserExtensions:
    @staticmethod
    def isInteger(text):
        try:
            int(text)
            return True
        except ValueError:
            return False

    @staticmethod
    def isFolder(type, flags):
        # Проверка, что тип папки равен 1, а константа равна 0
        return type == '1' and flags == '0'

    @staticmethod
    def isTemplate(type, flags):
        # Проверка, что тип шаблона равен 0, а флаги равны 0 или 1
        return type == '0' and flags in {'0', '1'}