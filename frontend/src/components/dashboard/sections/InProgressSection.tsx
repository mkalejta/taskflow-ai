import styles from "./section.module.css";
import Task from "../task/Task";
import { useTasks } from "@/hooks/useTasks";

export default function InProgressSection() {
    const { getInProgressTasks } = useTasks();
    const tasks = getInProgressTasks();

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