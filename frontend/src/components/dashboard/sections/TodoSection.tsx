import styles from "./section.module.css";
import Task from "../task/Task";
import { useTasks } from "@/hooks/useTasks";

export default function TodoSection() {
    const { getTodoTasks } = useTasks();
    const tasks = getTodoTasks();

    return (
        <div className={styles.container}>
            <div className={styles.tasks}>
                {tasks.map((task) =>                     
                    <Task key={task.id} task={task}/>
                )}
            </div>
        </div>
    );
}