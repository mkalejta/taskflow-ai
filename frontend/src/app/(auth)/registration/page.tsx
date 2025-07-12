'use client';

import { Button } from "@/components/ui/button/Button";
import styles from "./registration.module.css";
import { useRouter } from "next/navigation";

export default function Registration() {
  const router = useRouter();
  const confirm = () => {
    alert("Rejestracja zakończona sukcesem!");
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Dołącz do TaskFlow AI</h1>
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
          
          <label htmlFor="email" className={styles.label}>E-mail:</label>
          <input 
            id="email"
            type="email" 
            className={styles.input}
            placeholder="Wprowadź email"
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
          
          <label htmlFor="confirm-password" className={styles.label}>Confirm password:</label>
          <input 
            id="confirm-password"
            type="password" 
            className={styles.input}
            placeholder="Potwierdź hasło"
            required
          />
        </form>
        
        <div className={styles.buttons}>
          <Button title="Masz już konto?" variant="outline" onClick={() => router.push("/login")} />
          <Button title="Zarejestruj się" variant="nav" onClick={confirm}/>
        </div>
      </div>
    </div>
  );
}