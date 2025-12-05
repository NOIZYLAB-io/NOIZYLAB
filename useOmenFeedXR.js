/**
 * useOmenFeedXR - Live Omen Stats for VR
 * =======================================
 * Fetches HP Omen stats for 3D visualization.
 */

import { useState, useEffect } from "react";

const API_URL = "http://localhost:8080/remote/omen/live";

export default function useOmenFeedXR() {
  const [stats, setStats] = useState({
    cpu_usage: 0,
    ram_usage: 0,
    disk_usage: 0,
    temp: 50,
    device: "HP Omen",
    status: "connecting"
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        
        if (data.error) {
          setStats(prev => ({ ...prev, status: "offline" }));
        } else {
          setStats({ ...data, status: "online" });
        }
      } catch (error) {
        // Use mock data if server unavailable
        setStats(prev => ({
          ...prev,
          status: "mock",
          cpu_usage: 30 + Math.random() * 20,
          ram_usage: 40 + Math.random() * 20,
          temp: 55 + Math.random() * 15
        }));
      }
    };

    fetchStats();
    const interval = setInterval(fetchStats, 2000);

    return () => clearInterval(interval);
  }, []);

  return stats;
}

