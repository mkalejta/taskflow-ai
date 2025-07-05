'use client';

import { useState, useEffect } from "react";
import styles from "./dashboard.module.css";
import { AllSection, InProgressSection, DoneSection, TodoSection } from "@/components/dashboard/sections";
import { TaskStatus } from "@/types/enums";
import FilterBar from "@/components/dashboard/filterbar/FilterBar";
import { Button } from "@/components/ui/button/Button";

type DashboardSection = 'All' | TaskStatus;

const sections = {
    'All': <AllSection/>,
    [TaskStatus.IN_PROGRESS]: <InProgressSection/>,
    [TaskStatus.DONE]: <DoneSection/>,
    [TaskStatus.TODO]: <TodoSection/>
};

export default function Dashboard() {
    const [currentSection, setCurrentState] = useState<DashboardSection>('All');

    // Load saved state from localStorage
    useEffect(() => {
        const savedSection = localStorage.getItem('dashboardSection') as DashboardSection;
        if (savedSection && savedSection in sections) {
            setCurrentState(savedSection);
        }
    }, []);

    // Save state to localStorage
    const handleSectionChange = (section: DashboardSection) => {
        setCurrentState(section);
        localStorage.setItem('dashboardSection', section);
    };

    return (
        <div className={styles.container}>
            <div className={styles.top}>
                <h1>Dashboard</h1>
                <Button title="MK" variant="profile"/>
            </div>
            <FilterBar 
                currentSection={currentSection} 
                setCurrentState={handleSectionChange}
            />
            <div className={styles.main}>
                {sections[currentSection]}
            </div>
        </div>
    );
}