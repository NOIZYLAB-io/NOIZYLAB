import { create } from 'zustand'

export const useSystemStore = create((set) => ({
  snapshot: {},
  logs: [],
  devices: [],
  customers: [],
  sessions: [],
  
  setSnapshot: (data) => set({ snapshot: data }),
  addLog: (log) => set((state) => ({ logs: [log, ...state.logs].slice(0, 50) })),
  setDevices: (data) => set({ devices: data }),
  setCustomers: (data) => set({ customers: data }),
  setSessions: (data) => set({ sessions: data }),
}))

