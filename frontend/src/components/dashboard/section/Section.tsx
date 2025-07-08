import styles from "./section.module.css";
import Task from "../task/Task";
import { useTasks } from "@/hooks/useTasks";
import type { Task as TaskType } from "@/types";
import { TaskStatus } from "@/types/enums";

type DashboardSection = 'All' | TaskStatus;

interface SectionProps {
    currentSection: DashboardSection;
    onTaskSelect: (task: TaskType) => void;
}

export default function Section({ currentSection, onTaskSelect }: SectionProps) {
    const { getTasksByStatus, getAllTasks } = useTasks();
    const tasks = (currentSection === 'All') ? getAllTasks() : getTasksByStatus(currentSection);

    return (
        <div className={styles.container}>
            <div className={styles.tasks}>
                {tasks.map((task) =>                     
                    <Task 
                        key={task.id} 
                        task={task}
                        onTaskSelect={onTaskSelect}
                    />
                )}
            </div>
        </div>
    );
}