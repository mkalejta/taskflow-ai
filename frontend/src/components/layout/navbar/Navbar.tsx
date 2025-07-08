'use client';

import styles from "./navbar.module.css";
import { FaTasks } from "react-icons/fa";
import { Button } from "@/components/ui/button/Button";
import { IoChevronForward } from "react-icons/io5";
import { useRouter } from "next/navigation";

export default function Header() {
  const templateOptions = ["Kanban", "Step list", "Visualisation"]; // karuzela z tymi templatami i zdjęciami
  const router = useRouter();

  return (
    <div className={styles.container}>
      <div className={styles.logo}>
        <FaTasks size={30} /> {/* Docelowo tu będzie logo*/}
        <h1>Taskflow AI</h1>
      </div>
      <div className={styles.nav}>
        <div
          className={styles.metaItem}
          onClick={() => router.push("/chat")}
        >
          Chat
        </div>
        <div
          className={styles.metaItem}
          onClick={() => router.push("/templates")}
        >
          Templates
        </div>
        <div
          className={styles.metaItem}
          onClick={() => router.push("/about")}
        >
          About us
        </div>
      </div>
      <Button title="Get started" variant="nav" icon={<IoChevronForward />}/>
    </div>
  );
}