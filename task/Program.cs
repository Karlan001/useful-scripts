// Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, 
// длина которых меньше, либо равна 3 символам. 
// Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

void printArray(string[] arr) // Выводим массив на печать.
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write($"{arr[i]}\t");
    }
    Console.WriteLine();
}

int getLengthArr(string[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            count += 1;
        }
    }
    return count;
}

string[] newArray(string[] arr)
{
    string[] newArray = new string[getLengthArr(arr)];
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            newArray[count] = arr[i];
            count += 1;
        }
    }
    return newArray;
}

string[] array = {"Russia", "Denmark", "Kazan", "or", "and"};
printArray(newArray(array));


