'use client';

import { useState, useEffect, useRef } from 'react';
import { IoChevronBack, IoChevronForward } from 'react-icons/io5';
import styles from './carousel.module.css';

type CarouselItem = {
  id: number;
  title: string;
  description: string;
  videoSrc: string;
  startTime: number;
  endTime: number;
};

type CarouselProps = {
  items: CarouselItem[];
  autoPlay?: boolean;
  autoPlayInterval?: number;
};

export default function Carousel({ items, autoPlay = true, autoPlayInterval = 5000 }: CarouselProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const videoRefs = useRef<(HTMLVideoElement | null)[]>([]);

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % items.length);
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + items.length) % items.length);
  };

  const goToSlide = (index: number) => {
    setCurrentIndex(index);
  };

  // Handle video time control
  const handleVideoLoad = (videoElement: HTMLVideoElement, item: CarouselItem, index: number) => {
    if (index === currentIndex) {
      videoElement.currentTime = item.startTime;
      videoElement.play();
    }
  };

  const handleTimeUpdate = (videoElement: HTMLVideoElement, item: CarouselItem) => {
    if (videoElement.currentTime >= item.endTime) {
      videoElement.currentTime = item.startTime; // Loop fragment
    }
  };

  // Reset video when slide changes
  useEffect(() => {
    const currentVideo = videoRefs.current[currentIndex];
    const currentItem = items[currentIndex];
    
    if (currentVideo && currentItem) {
      // Pause all videos first
      videoRefs.current.forEach((video, index) => {
        if (video && index !== currentIndex) {
          video.pause();
        }
      });

      // Set current video to start time and play
      currentVideo.currentTime = currentItem.startTime;
      currentVideo.play().catch(console.error);
    }
  }, [currentIndex, items]);

  // Auto play
  useEffect(() => {
    if (!autoPlay) return;

    const interval = setInterval(nextSlide, autoPlayInterval);
    return () => clearInterval(interval);
  }, [autoPlay, autoPlayInterval, nextSlide]);

  return (
    <div className={styles.carousel}>
      <div className={styles.carouselContainer}>
        <div 
          className={styles.carouselTrack}
          style={{ transform: `translateX(-${currentIndex * 100}%)` }}
        >
          {items.map((item, index) => (
            <div key={item.id} className={styles.carouselSlide}>
              <div className={styles.example}>
                <div className={styles.content}>
                  <h2 className={styles.header2}>{item.title}</h2>
                  <p>{item.description}</p>
                </div>
                <video 
                  ref={(el) => {
                    videoRefs.current[index] = el;
                  }}
                  width="600" 
                  height="400" 
                  controls 
                  loop={false}
                  muted 
                  preload="metadata" 
                  className={styles.exampleVideo}
                  onLoadedData={(e) => handleVideoLoad(e.currentTarget, item, index)}
                  onTimeUpdate={(e) => handleTimeUpdate(e.currentTarget, item)}
                  onEnded={(e) => {
                    // When fragment ends, restart from beginning of fragment
                    e.currentTarget.currentTime = item.startTime;
                    e.currentTarget.play();
                  }}
                >
                  <source src={item.videoSrc} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
              </div>
            </div>
          ))}
        </div>

        {/* Navigation buttons */}
        <button 
          className={`${styles.carouselButton} ${styles.prevButton}`}
          onClick={prevSlide}
          aria-label="Previous slide"
        >
          <IoChevronBack />
        </button>
        <button 
          className={`${styles.carouselButton} ${styles.nextButton}`}
          onClick={nextSlide}
          aria-label="Next slide"
        >
          <IoChevronForward />
        </button>

        {/* Dots indicator */}
        <div className={styles.dotsContainer}>
          {items.map((_, index) => (
            <button
              key={index}
              className={`${styles.dot} ${index === currentIndex ? styles.activeDot : ''}`}
              onClick={() => goToSlide(index)}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </div>
  );
}