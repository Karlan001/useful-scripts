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

string[] createArr(string[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            count += 1;
        }
    }
    string[] newArray = new string[count];
    return newArray;
}

string[] newArray(string[] arr, string[] newArr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            newArr[count] = arr[i];
            count += 1;
        }
    }
    return newArr;
}

string[] array = {"Russia", "Denmark", "Kazan", "or", "and", "go"};
string[] newArr = createArr(array);
printArray(newArray(array, newArr));
