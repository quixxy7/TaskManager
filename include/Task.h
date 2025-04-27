#ifndef TASK_H
#define TASK_H

#include <string>
#include <stdexcept>
#include "nlohmann/json.hpp"
using json = nlohmann::json;

enum class TaskStatus {
    NotStarted,
    InProgress,
    Completed
};

class Task {
    private:
        std::string name;
        std::string description;
        TaskStatus status;
    public:
        Task(const std::string &name,
             const std::string &description = "",
             TaskStatus status = TaskStatus::NotStarted);

        std::string getName() const;
        std::string getDescription() const;
        TaskStatus getStatus() const;

        void setName(const std::string &newName);
        void setDescription(const std::string &newDescription);
        void setStatus(TaskStatus newStatus);

        static std::string statusToString(TaskStatus status);
        static TaskStatus stringToStatus(const std::string &str);
};

#endif
