import styles from "./task.module.css";
import { FaCheck } from "react-icons/fa6";
import { RiProgress1Line, RiProgress3Line,
    RiProgress5Line, RiProgress7Line
} from "react-icons/ri";
import { IoCheckmarkDone } from "react-icons/io5";
import type { Task } from "@/types";
import { TaskStatus } from "@/types/enums";
import { useRouter } from "next/navigation";

type TaskProps = {
    task: Task;
}

const status_icons = {
    [TaskStatus.TODO]: <FaCheck className={styles.status_todo}/>,
    [TaskStatus.IN_PROGRESS]: <RiProgress1Line className={styles.status_inprogress}/>,
    [TaskStatus.DONE]: <IoCheckmarkDone className={styles.status_done}/>
};

export default function Task({ task }: TaskProps) {
    const router = useRouter();

    return (
        <button onClick={() => router.push(`/task-details/${task.id}`)} className={styles.container}>
            <div className={styles.icon}>
                {status_icons[task.status]}
            </div>
            <div className={styles.content}>
                <h3>{task.title}</h3>
                <p>{task.description}</p>
                <span>Priority: {task.priority}</span>
            </div>
        </button>
    );
}