# STFileParserExtensions.py
class STFileParserExtensions:
    @staticmethod
    def isInteger(text):
        print(f"Checking if '{text}' is integer")
        return text.isdigit() 

    @staticmethod
    def isFolder(type, flags):
        # Проверка, что тип папки равен 1, а константа равна 0
        return type == '1' and flags == '0'

    @staticmethod
    def isTemplate(type, flags):
        # Проверка, что тип шаблона равен 0, а флаги равны 0 или 1
        return type == '0' and flags in {'0', '1'}
    
if __name__ == "__main__":
    print("Self-test:")
    print(STFileParserExtensions.isInteger("123"))  # True
    print(STFileParserExtensions.isInteger("abc"))  # False
    print(STFileParserExtensions.isFolder("1", "0"))  # True
    print(STFileParserExtensions.isTemplate("0", "1"))  # True