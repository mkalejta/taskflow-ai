'use client';

import { useState, useEffect, useRef } from "react";
import styles from "./dashboard.module.css";
import Section from "@/components/dashboard/section/Section";
import { TaskStatus } from "@/types/enums";
import FilterBar from "@/components/dashboard/filterbar/FilterBar";
import TaskDetails from "@/components/dashboard/task-details/TaskDetails";
import type { Task } from "@/types";

type DashboardSection = 'All' | TaskStatus;

interface ViewState {
    section: DashboardSection;
    scrollPosition: number;
    selectedTask?: Task;
}

export default function Dashboard() {
    const [currentSection, setCurrentSection] = useState<DashboardSection>('All');
    const [selectedTask, setSelectedTask] = useState<Task | null>(null);
    const [viewState, setViewState] = useState<ViewState | null>(null);
    const containerRef = useRef<HTMLDivElement>(null);

    // Load saved state from localStorage
    useEffect(() => {
        const savedSection = localStorage.getItem('dashboardSection') as DashboardSection;
        if (savedSection && (savedSection === 'All' || Object.values(TaskStatus).includes(savedSection as TaskStatus))) {
            setCurrentSection(savedSection);
        }
    }, []);

    // Save state to localStorage
    const handleSectionChange = (section: DashboardSection) => {
        setCurrentSection(section);
        setSelectedTask(null);
        localStorage.setItem('dashboardSection', section);
    };

    // Handle task selection
    const handleTaskSelect = (task: Task) => {
        // Save current view state
        const scrollPosition = containerRef.current?.scrollTop || 0;
        setViewState({
            section: currentSection,
            scrollPosition,
            selectedTask: task
        });
        setSelectedTask(task);
    };

    // Handle back to list
    const handleBackToList = () => {
        setSelectedTask(null);
        
        // Restore scroll position
        if (viewState && containerRef.current) {
            setTimeout(() => {
                containerRef.current!.scrollTop = viewState.scrollPosition;
            }, 0);
        }
    };

    return (
        <div className={styles.content}>
            <div className={styles.top}>
                <h1>Dashboard</h1>
            </div>
            
            {!selectedTask && (
                <FilterBar 
                    currentSection={currentSection} 
                    setCurrentState={handleSectionChange}
                />
            )}
            
            <div className={styles.main} ref={containerRef}>
                {selectedTask ? (
                    <TaskDetails 
                        task={selectedTask} 
                        onBack={handleBackToList}
                    />
                ) : (
                    <Section currentSection={currentSection} onTaskSelect={handleTaskSelect}/>
                )}
            </div>
        </div>
    );
}