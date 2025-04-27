#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include <string>
#include <vector>
#include <stdexcept>
#include "Task.h"
#include <nlohmann/json.hpp>
using json = nlohmann::json;

class TaskManager {
    private:
        std::vector<Task> tasks;
    public:
        void addTask(const Task &task);
        void removeTask(size_t index);
        void updateTask(size_t index);

        void showTasks() const;
        void sortTasksBy();
        void filterTasksBy();

        void loadFromJson(const std::string &filename);
        voud saveToJson(const std::string &filename) const;

        void clearAllTasks();
}
#endif
