import Sidebar from "@/components/layout/sidebar/Sidebar";
import styles from "./dashboard.module.css";

export default function DashboardLayout({
    children
}: Readonly<{
    children:React.ReactNode;
}>) {
    return (
        <div className={styles.container}>
            <Sidebar/>
            {children}
        </div>
    )
}