'use client';

import styles from "./button.module.css";

type ButtonProps = {
    title?: string;
    onClick?: () => void;
    variant?: 'default' | 'profile' | 'nav' | 'active' | 'sidebar';
}

export const Button = ({title, onClick, variant = "default"}: ButtonProps) => {
    const buttonClass = `${styles.button} ${styles[variant]}`;

    return (
        <button className={buttonClass} onClick={onClick} >{title}</button>
    )
}