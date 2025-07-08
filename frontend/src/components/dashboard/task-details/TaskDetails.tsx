import styles from "./task-details.module.css";
import { Button } from "@/components/ui/button/Button";
import { IoArrowBack } from "react-icons/io5";
import type { Task } from "@/types";

interface TaskDetailsProps {
    task: Task;
    onBack: () => void;
}

export default function TaskDetails({ task, onBack }: TaskDetailsProps) {
    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <Button
                    title=""
                    variant="back"
                    onClick={onBack}
                    icon={<IoArrowBack />}
                />
                <h1>{task.title}</h1>
            </div>
            
            <div className={styles.content}>
                <div className={styles.section}>
                    <h2>Description</h2>
                    <p>{task.description}</p>
                </div>
                
                <div className={styles.meta}>
                    <div className={styles.metaItem}>
                        <span className={styles.label}>Author:</span>
                        <span>{task.author}</span>
                    </div>
                    
                    <div className={styles.metaItem}>
                        <span className={styles.label}>Priority:</span>
                        <span className={styles[`priority-${task.priority.toLowerCase()}`]}>
                            {task.priority}
                        </span>
                    </div>
                    
                    <div className={styles.metaItem}>
                        <span className={styles.label}>Status:</span>
                        <span className={styles[`status-${task.status.toLowerCase().replace(' ', '-')}`]}>
                            {task.status}
                        </span>
                    </div>
                    
                    <div className={styles.metaItem}>
                        <span className={styles.label}>Created:</span>
                        <span>{new Date(task.createdAt).toLocaleDateString()}</span>
                    </div>
                    
                    {task.updatedAt && (
                        <div className={styles.metaItem}>
                            <span className={styles.label}>Updated:</span>
                            <span>{new Date(task.updatedAt).toLocaleDateString()}</span>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}