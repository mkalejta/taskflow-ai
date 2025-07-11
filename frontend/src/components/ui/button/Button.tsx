'use client';

import styles from "./button.module.css";

type ButtonProps = {
    title: string;
    onClick?: () => void;
    variant?: 'default' | 'nav' | 'active' | 'back' | 'sidebar' | 'outline';
    icon?: React.ReactNode;
}

export function Button({ title, onClick, variant = 'default', icon }: ButtonProps) {
    const buttonClass = `${styles.button} ${styles[variant]}`;
    
    return (
        <button className={buttonClass} onClick={onClick}>
            {icon && <span className={styles.icon}>{icon}</span>}
            {title && <span>{title}</span>}
        </button>
    );
}