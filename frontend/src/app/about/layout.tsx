import styles from "./about.module.css";

export default function AboutLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className={styles.container}>
      <main>
        {children}
      </main>
    </div>
  );
}