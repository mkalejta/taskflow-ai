'use client';

import { Button } from "@/components/ui/button/Button";
import styles from "./login.module.css";
import { useRouter } from "next/navigation";

export default function Login() {
  const router = useRouter();
  const confirm = () => {
    alert("zalogowano!");
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Zaloguj się do TaskFlow AI</h1>
      <div className={`${styles.content} border-purple`}>
        <form className={styles.form}>
          <label htmlFor="login" className={styles.label}>Login:</label>
          <input 
            id="login"
            type="text" 
            className={styles.input}
            placeholder="Wprowadź login"
            required
          />
          
          <label htmlFor="password" className={styles.label}>Password:</label>
          <input 
            id="password"
            type="password" 
            className={styles.input}
            placeholder="Wprowadź hasło"
            required
          />
        </form>
        
        <div className={styles.buttons}>
          <Button title="Nie masz jeszce konta?" variant="outline" onClick={() => router.push("/registration")} />
          <Button title="Zaloguj się" variant="nav" onClick={confirm}/>
        </div>
      </div>
    </div>
  );
}