import express from 'express';
import cors from 'cors';
import http from 'http';
import { Server as SocketServer } from 'socket.io';

import authRoutes from './routes/auth';
import diagnosticsRoutes from './routes/diagnostics';
import devicesRoutes from './routes/devices';
import sessionRoutes from './routes/session';
import pricingRoutes from './routes/pricing';
import reportsRoutes from './routes/reports';

const app = express();
app.use(express.json());
app.use(cors());

// ROUTES
app.use('/auth', authRoutes);
app.use('/diagnostics', diagnosticsRoutes);
app.use('/devices', devicesRoutes);
app.use('/session', sessionRoutes);
app.use('/pricing', pricingRoutes);
app.use('/reports', reportsRoutes);

// HTTP + WS SERVER
const httpServer = http.createServer(app);
export const io = new SocketServer(httpServer, {
  cors: { origin: '*' }
});

io.on('connection', socket => {
  console.log('🔥 Realtime connection:', socket.id);
  
  socket.on('disconnect', () => {
    console.log('📡 Client disconnected:', socket.id);
  });
});

const PORT = process.env.PORT || 5000;
httpServer.listen(PORT, () => {
  console.log('╔═══════════════════════════════════════════════════════════════╗');
  console.log('║                                                               ║');
  console.log('║          🔥 NOIZY.AI BACKEND ONLINE 🔥                        ║');
  console.log('║                                                               ║');
  console.log(`║          Port: ${PORT}                                            ║`);
  console.log('║          Fish Music Inc - CB_01                               ║');
  console.log('║                                                               ║');
  console.log('╚═══════════════════════════════════════════════════════════════╝');
  console.log('');
  console.log('🔥 GORUNFREE! 🎸🔥');
  console.log('');
});
