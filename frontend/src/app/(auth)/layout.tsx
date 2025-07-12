import styles from "./auth.module.css";
import Navbar from "@/components/layout/navbar/Navbar";

export default function AuthLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <div className={styles.container}>
            <Navbar />
            {children}
        </div>
    )
}