from ANTLR4.STFileListener import STFileListener

'''
Модуль STFileCustomListener является пользовательским обработчиком событий для ANTLR-парсера, 
который наследуется от базового класса STFileListener. Его основная задача — проверять корректность 
параметров шаблонов в структуре файла .st и выводить предупреждения при обнаружении проблем.

Ключевые особенности:
Назначение: 
    Проверка структуры шаблонов в файле, особенно на наличие пустых параметров.
Интеграция: 
    Работает совместно с парсером, сгенерированным ANTLR из грамматики STFile.g4.
Гибкость: 
    Может быть расширен для добавления дополнительных проверок.
'''

class STFileCustomListener(STFileListener):
    def enterTemplateHeader(self, ctx):
        '''
        Обработка шаблона с проверкой пустых параметров
        Вызывается при входе в правило templateHeader грамматики.
        Параметры:
            ctx: Контекст узла дерева разбора, содержащий информацию о текущем шаблоне.
        '''
        try:
            # Безопасное извлечение имени шаблона
            template_name = ctx.name.text[1:-1] if ctx.name and ctx.name.text else "UNNAMED"
            # Проверка param1
            if ctx.param1:
                param1_content = ctx.param1.text[1:-1]  # Удаляем кавычки
                if not param1_content.strip():
                    print(f"Пустой param1 в шаблоне: {template_name}")
            else:
                print(f"Отсутствует param1 в шаблоне: {template_name}")
            
            # Проверка codeBlock
            if ctx.codeBlock:
                code_content = ctx.codeBlock.text[1:-1]  # Удаляем кавычки
                if not code_content.strip():
                    print(f"Пустой codeBlock в шаблоне: {template_name}")
            else:
                print(f"Отсутствует codeBlock в шаблоне: {template_name}")

        except Exception as e:
            print(f"Ошибка при обработке шаблона: {str(e)}")


        '''
        # Проверка на пустой param1 (убираем внешние кавычки)
        param1_content = ctx.param1.text[1:-1]  # Удаляем обрамляющие "
        if not param1_content:
            print(f"Обнаружен пустой param1 в шаблоне: {ctx.name.text[1:-1]}")
        
        # Проверка на пустой codeBlock
        code_content = ctx.codeBlock.text[1:-1]  # Удаляем обрамляющие "
        if not code_content:
            print(f"Пустой codeBlock в шаблоне: {ctx.name.text[1:-1]}") '''