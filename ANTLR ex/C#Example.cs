using System;

class Program
{
    static void Main()
    {
        // Инициализация списка чисел
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Перебор списка с использованием цикла for
        foreach (int number in numbers)
        {
            // Проверка, является ли число четным или нечетным с помощью ветвления if-else
            if (number % 2 == 0)
            {
                Console.WriteLine($"{number} is even");  // Четное число
            }
            else
            {
                Console.WriteLine($"{number} is odd");  // Нечетное число
            }
        }
    }
}
