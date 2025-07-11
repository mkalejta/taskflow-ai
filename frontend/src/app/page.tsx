"use client";

import styles from "@/styles/landing.module.css";
import { Button } from "@/components/ui/button/Button";
import { useRouter } from "next/navigation";
import Navbar from "@/components/layout/navbar/Navbar";
import Image from "next/image";
import { FaRobot, FaBolt, FaShieldAlt } from "react-icons/fa";
import Carousel from "@/components/ui/carousel/Carousel";
import { useRef } from 'react';
import { useScrollAnimation } from "@/hooks/useScrollAnimation";

export default function Home() {
  const router = useRouter();
  const aboutRef = useRef<HTMLElement | null>(null);
  const { elementRef: featuresRef, isVisible: featuresVisible } = useScrollAnimation(0.2);
  const { elementRef: aboutAnimationRef, isVisible: aboutVisible } = useScrollAnimation(0.3);
  
  const slideDown = () => {
    aboutRef.current?.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  };

  const carouselItems = [
    {
      id: 1,
      title: "Dashboard Overview",
      description: "Uzyskaj pełny przegląd swoich zadań, projektów i postępów w jednym miejscu. Intuicyjny dashboard pozwala na szybkie zarządzanie wszystkimi aspektami pracy.",
      videoSrc: "/example1.mp4",
      startTime: 0,
      endTime: 7,
    },
    {
      id: 2,
      title: "AI-Powered Analytics",
      description: "Wykorzystaj moc sztucznej inteligencji do analizy produktywności zespołu. Otrzymuj inteligentne sugestie i rekomendacje dla lepszej organizacji pracy.",
      videoSrc: "/example1.mp4",
      startTime: 7,
      endTime: 14,
    },
    {
      id: 3,
      title: "Real-time Collaboration",
      description: "Współpracuj z zespołem w czasie rzeczywistym. Udostępniaj zadania, komentarze i pliki bez przeszkód. Wszyscy są zawsze na bieżąco.",
      videoSrc: "/example1.mp4",
      startTime: 14,
      endTime: 21,
    },
  ];

  const templateOptions = ["Kanban", "Step list", "Visualisation"]; // karuzela z tymi templatami i zdjęciami

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

        <section 
          ref={featuresRef} 
          className={`${styles.features} ${featuresVisible ? styles.featuresVisible : ''}`}
        >
          {[
            { icon: FaRobot, title: "AI-Powered", desc: "Inteligentne sugestie i automatyzacja zadań", delay: 0.1 },
            { icon: FaBolt, title: "Szybkość", desc: "Błyskawiczne ładowanie i responsywność", delay: 0.3 },
            { icon: FaShieldAlt, title: "Bezpieczeństwo", desc: "Twoje dane są zawsze chronione", delay: 0.5 }
          ].map((feature, index) => (
            <div 
              key={index}
              className={`${styles.feature} ${featuresVisible ? styles.featureVisible : ''}`} 
              style={{ 
                '--delay': `${feature.delay}s` 
              } as React.CSSProperties}
            >
              <div className={styles.featureIcon}>
                <feature.icon />
              </div>
              <h3 className={styles.featureTitle}>{feature.title}</h3>
              <p className={styles.featureDescription}>{feature.desc}</p>
            </div>
          ))}
        </section>

        <section 
          ref={(el) => {
            aboutRef.current = el;
            aboutAnimationRef.current = el;
          }} 
          className={`${styles.about} ${aboutVisible ? styles.aboutVisible : ''}`}
        >
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
