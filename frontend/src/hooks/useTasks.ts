import { useMemo } from 'react';
import rawTasks from '../data/data.json';
import { convertRawTask } from '../lib/converters';
import { Task, TaskStatus } from '../types';

export const useTasks = () => {
    const tasks = useMemo(() => 
        rawTasks.map(convertRawTask), 
        []
    );

    const getTasksByStatus = (status: TaskStatus): Task[] => {
        return tasks.filter(task => task.status === status);
    };

    const getAllTasks = (): Task[] => tasks;
    const getTodoTasks = (): Task[] => getTasksByStatus(TaskStatus.TODO);
    const getInProgressTasks = (): Task[] => getTasksByStatus(TaskStatus.IN_PROGRESS);
    const getDoneTasks = (): Task[] => getTasksByStatus(TaskStatus.DONE);

    return {
        tasks,
        getAllTasks,
        getTodoTasks,
        getInProgressTasks,
        getDoneTasks,
        getTasksByStatus
    };
};