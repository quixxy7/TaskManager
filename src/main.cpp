#include "Task.h"

#include <iostream>
#include <fstream>

int main() {
    try {
        // Тест 1: Создание задачи с минимальными параметрами
        Task task1("Позвонить маме");
        std::cout << "Task 1: " << task1.getName()
                  << " | Status: " << Task::statusToString(task1.getStatus())
                  << " | Description: " << (task1.getDescription().empty() ? "N/A" : task1.getDescription())
                  << std::endl;

        // Тест 2: Создание задачи с описанием
        Task task2("Купить продукты", "Молоко, хлеб, яйца");
        std::cout << "Task 2: " << task2.getName()
                  << " | Status: " << Task::statusToString(task2.getStatus())
                  << " | Description: " << task2.getDescription()
                  << std::endl;

        // Тест 3: Изменение статуса и описания
        task1.setStatus(TaskStatus::InProgress);
        task1.setDescription("Позвонить до 18:00");
        std::cout << "Task 1 (updated): " << task1.getName()
                  << " | Status: " << Task::statusToString(task1.getStatus())
                  << " | Description: " << task1.getDescription()
                  << std::endl;

        // Тест 4: Преобразование строки в статус
        std::string statusStr = "Completed";
        TaskStatus status = Task::stringToStatus(statusStr);
        Task task3("Завершить проект", "Рефакторинг кода", status);
        std::cout << "Task 3: " << task3.getName()
                  << " | Status: " << Task::statusToString(task3.getStatus())
                  << std::endl;

        // Тест 5: Некорректный статус (должно выбросить исключение)
        TaskStatus invalid = Task::stringToStatus("Unknown"); // Раскомментируй для проверки

    } catch (const std::exception& e) {
        std::cerr << "Ошибка: " << e.what() << std::endl;
    }

    return 0;
}
