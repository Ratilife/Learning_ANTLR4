public class JavaExample {
    public static void main(String[] args) {
        // Инициализация списка чисел
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Перебор списка с использованием цикла for-each
        for (int number : numbers) {
            // Проверка, является ли число четным или нечетным с помощью ветвления if-else
            if (number % 2 == 0) {
                System.out.println(number + " is even");  // Четное число
            } else {
                System.out.println(number + " is odd");  // Нечетное число
            }
        }
    }
}
