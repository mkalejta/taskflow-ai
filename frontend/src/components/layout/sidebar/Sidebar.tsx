'use client';

import { Button } from "../../ui/button/Button";
import { useRouter } from "next/navigation";
import styles from "./sidebar.module.css";
import { FaTasks } from "react-icons/fa";

export default function Sidebar() {
    const router = useRouter();

    return (
        <div className={styles.container}>
            <div className={styles.top} onClick={() => router.push("/")}>
                <FaTasks size={30}/> {/* Docelowo tu będzie logo*/}
                <h1>Taskflow AI</h1>
            </div>
            <div className={styles.mid}>
                <div className={styles.new}>New Chat +</div>
                <div>Dashboard</div>
                <div>Templates</div>
                <div>History</div>
            </div>
            <div className={styles.bottom}>
                <Button title="Login" variant="sidebar" onClick={() => router.push("/login")}/>
                <Button title="Register" variant="sidebar" onClick={() => router.push("/registration")}/>
            </div>
        </div>
    )
}