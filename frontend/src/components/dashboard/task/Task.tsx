import styles from "./task.module.css";
import { FaCheck } from "react-icons/fa6";
import { RiProgress1Line, RiProgress3Line,
    RiProgress5Line, RiProgress7Line
} from "react-icons/ri";
import { IoCheckmarkDone } from "react-icons/io5";
import type { Task } from "@/types";
import { TaskStatus } from "@/types/enums";

type TaskProps = {
    task: Task;
    onTaskSelect: (task: Task) => void;
}

const status_icons = {
    [TaskStatus.TODO]: <FaCheck className={`${styles.status_todo} ${styles.status}`}/>,
    [TaskStatus.IN_PROGRESS]: <RiProgress1Line className={`${styles.status_inprogress} ${styles.status}`}/>,
    [TaskStatus.DONE]: <IoCheckmarkDone className={`${styles.status_done} ${styles.status}`}/>
};

export default function Task({ task, onTaskSelect }: TaskProps) {
    const handleTaskClick = () => {
        onTaskSelect(task);
    };

    return (
        <button onClick={handleTaskClick} className={styles.container}>
            <div className={styles.icon}>
                {status_icons[task.status]}
            </div>
            <div className={styles.content}>
                <h3>{task.title}</h3>
                <p>{task.description}</p>
                <div className={styles.metaItem}>
                    <span className={styles.label}>Priority:</span>
                    <span className={`${styles[`priority-${task.priority.toLowerCase()}`]} ${styles.priority}`}>
                        {task.priority}
                    </span>
                </div>
            </div>
        </button>
    );
}