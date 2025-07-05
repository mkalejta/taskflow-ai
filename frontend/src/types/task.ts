import { TaskPriority, TaskStatus } from './enums';

export interface Task {
    id: number;
    author: string;
    title: string;
    description: string;
    priority: TaskPriority;
    status: TaskStatus;
    assignedTo: string | null;
    dueDate: string | null;
    tags: string[] | null;
    createdAt: string;
    updatedAt: string | null;
}

export interface RawTask {
    id: number;
    author: string;
    title: string;
    description: string;
    priority: string;
    status: string;
    assignedTo: string | null;
    dueDate: string | null;
    tags: string[] | null;
    createdAt: string;
    updatedAt: string | null;
}