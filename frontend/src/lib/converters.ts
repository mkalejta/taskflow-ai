import { TaskPriority, TaskStatus } from '../types/enums';

// Function to convert string values to TaskPriority enum
export const convertToPriority = (priority: string): TaskPriority => {
    const found = Object.values(TaskPriority).find(p => p === priority);
    return found || TaskPriority.LOW;
};

// Function to convert string values to TaskStatus enum
export const convertToStatus = (status: string): TaskStatus => {
    const found = Object.values(TaskStatus).find(s => s === status);
    return found || TaskStatus.TODO;
};

// Function to convert raw task data to a structured format
export const convertRawTask = (rawTask: any) => ({
    ...rawTask,
    priority: convertToPriority(rawTask.priority),
    status: convertToStatus(rawTask.status),
    updatedAt: rawTask.updatedAt || null
});