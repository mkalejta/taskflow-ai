"use client";

import styles from "@/styles/landing.module.css";
import { Button } from "@/components/ui/button/Button";
import { useRouter } from "next/navigation";
import Navbar from "@/components/layout/navbar/Navbar";
import Image from "next/image";
import { FaRobot, FaBolt, FaShieldAlt } from "react-icons/fa";
import Carousel from "@/components/ui/carousel/Carousel";

export default function Home() {
  const router = useRouter();
  const slideDown = () => {};

  const carouselItems = [
    {
      id: 1,
      title: "Dashboard Overview",
      description:
        "Uzyskaj pełny przegląd swoich zadań, projektów i postępów w jednym miejscu. Intuicyjny dashboard pozwala na szybkie zarządzanie wszystkimi aspektami pracy.",
      videoSrc: "/example1.mp4",
      startTime: 0,
      endTime: 7,
    },
    {
      id: 2,
      title: "AI-Powered Analytics",
      description:
        "Wykorzystaj moc sztucznej inteligencji do analizy produktywności zespołu. Otrzymuj inteligentne sugestie i rekomendacje dla lepszej organizacji pracy.",
      videoSrc: "/example1.mp4",
      startTime: 7,
      endTime: 14,
    },
    {
      id: 3,
      title: "Real-time Collaboration",
      description:
        "Współpracuj z zespołem w czasie rzeczywistym. Udostępniaj zadania, komentarze i pliki bez przeszkód. Wszyscy są zawsze na bieżąco.",
      videoSrc: "/example1.mp4",
      startTime: 14,
      endTime: 21,
    },
  ];

  return (
    <>
      <Navbar />
      <main className={styles.container}>
        <section className={styles.hero}>
          <h1 className={styles.title}>
            Zarządzaj zadaniami z pomocą{" "}
            <span className={styles.accent}>AI</span>
          </h1>
          <p className={styles.description}>
            Taskflow AI to nowoczesna platforma do zarządzania zadaniami, która
            wykorzystuje sztuczną inteligencję do optymalizacji Twojej
            produktywności.
          </p>
          <div className={styles.actions}>
            <Button
              title="Rozpocznij za darmo"
              variant="nav"
              onClick={() => router.push("/dashboard")}
            />
            <Button
              title="Dowiedz się więcej"
              variant="outline"
              onClick={slideDown}
            />
          </div>
        </section>

        <section className={styles.features}>
          <div className={styles.feature}>
            <div className={styles.featureIcon}>
              <FaRobot />
            </div>
            <h3 className={styles.featureTitle}>AI-Powered</h3>
            <p className={styles.featureDescription}>
              Inteligentne sugestie i automatyzacja zadań
            </p>
          </div>
          <div className={styles.feature}>
            <div className={styles.featureIcon}>
              <FaBolt />
            </div>
            <h3 className={styles.featureTitle}>Szybkość</h3>
            <p className={styles.featureDescription}>
              Błyskawiczne ładowanie i responsywność
            </p>
          </div>
          <div className={styles.feature}>
            <div className={styles.featureIcon}>
              <FaShieldAlt />
            </div>
            <h3 className={styles.featureTitle}>Bezpieczeństwo</h3>
            <p className={styles.featureDescription}>
              Twoje dane są zawsze chronione
            </p>
          </div>
        </section>

        <section className={styles.about}>
          <h2 className={styles.header}>Na co pozwala TaskflowAI?</h2>
          <p>
            Poznaj możliwości naszej platformy poprzez interaktywne przykłady.
            Zobacz jak TaskflowAI może zrewolucjonizować sposób w jaki zarządzasz
            projektami i zadaniami.
          </p>
          <Image
            src="/dashboard_page.png"
            alt="Dashboard preview"
            width={800}
            height={600}
            className={styles.dashboardImage}
          />
        </section>

        <section className={styles.examples}>
          <h2 className={styles.header}>Zobacz TaskflowAI w akcji</h2>
          <Carousel
            items={carouselItems}
            autoPlay={true}
            autoPlayInterval={7000}
          />
        </section>
      </main>
    </>
  );
}
