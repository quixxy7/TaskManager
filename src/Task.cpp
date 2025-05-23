#include "Task.h"

Task::Task(const std::string &name,
           const std::string &description,
           TaskStatus status)
        : name(name), description(description), status(status) {}

std::string Task::getName() const { return name; }
std::string Task::getDescription() const { return description; }
TaskStatus Task::getStatus() const { return status; }

void Task::setName(const std::string &newName) { name = newName; }
void Task::setDescription(const std::string &newDescription) { description = newDescription; }
void Task::setStatus(TaskStatus newStatus) { status = newStatus; }

std::string Task::statusToString(TaskStatus status) {
    switch(status) {
        case TaskStatus::NotStarted: return "Not Started";
        case TaskStatus::InProgress: return "In Progress";
        case TaskStatus::Completed: return "Completed";
        default:
            throw std::invalid_argument("Unknown status");
    }
}

TaskStatus Task::stringToStatus(const std::string& str) {
    if (str == "Not Started") return TaskStatus::NotStarted;
    else if (str == "In Progress") return TaskStatus::InProgress;
    else if (str == "Completed") return TaskStatus::Completed;
    else
        throw std::invalid_argument("Invalid status string: " + str);
}
