import styles from "./section.module.css";
import Task from "../task/Task";
import { useTasks } from "../../../hooks/useTasks";

export default function AllSection() {
    const { getAllTasks } = useTasks();
    const tasks = getAllTasks();

    return (
        <div className={styles.container}>
            <div className={styles.tasks}>
                {tasks.map((task) =>                     
                    <Task key={task.id} task={task}/>
                )}
            </div>
        </div>
    )
}