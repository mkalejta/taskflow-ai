import styles from "./filterbar.module.css";
import { Button } from "@/components/ui/button/Button";
import { TaskStatus } from "@/types/enums";

type SectionKey = 'All' | TaskStatus;

type FilterBarProps = {
    currentSection: SectionKey;
    setCurrentState: (section: SectionKey) => void;
};

export default function FilterBar({ currentSection, setCurrentState }: FilterBarProps) {
    return (
        <>        
            <div className={styles.navbar}>
                <Button 
                    title="All" 
                    variant={currentSection === 'All' ? 'active' : 'nav'} 
                    onClick={() => setCurrentState('All')}
                />
                <Button 
                    title="In Progress" 
                    variant={currentSection === TaskStatus.IN_PROGRESS ? 'active' : 'nav'} 
                    onClick={() => setCurrentState(TaskStatus.IN_PROGRESS)}
                />
                <Button 
                    title="Done" 
                    variant={currentSection === TaskStatus.DONE ? 'active' : 'nav'} 
                    onClick={() => setCurrentState(TaskStatus.DONE)}
                />
                <Button 
                    title="Todo" 
                    variant={currentSection === TaskStatus.TODO ? 'active' : 'nav'} 
                    onClick={() => setCurrentState(TaskStatus.TODO)}
                />
                <label className={styles.checkbox}>Assigned To Me
                    <input type="checkbox"/>
                    <span className={styles.checkmark}></span>
                </label>
            </div>
        </>
    )
}