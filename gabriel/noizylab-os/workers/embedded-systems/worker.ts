import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { EMBEDDED_DB: D1Database; AI: any; }
const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// NOIZYLAB OS - EMBEDDED SYSTEMS WORKER
const EMBEDDED_SYSTEMS = {
    microcontrollers: {
        arduino: { name: 'Arduino', year: 2005, processor: 'ATmega', significance: 'Maker movement pioneer' },
        esp32: { name: 'ESP32', developer: 'Espressif', significance: 'WiFi/BT IoT standard' },
        esp8266: { name: 'ESP8266', developer: 'Espressif', significance: 'Cheap WiFi module' },
        stm32: { name: 'STM32', developer: 'STMicroelectronics', significance: 'ARM Cortex-M standard' },
        pic: { name: 'PIC', developer: 'Microchip', significance: 'Classic microcontroller' },
        avr: { name: 'AVR', developer: 'Atmel/Microchip', significance: 'Arduino foundation' },
        nrf52: { name: 'nRF52', developer: 'Nordic', significance: 'BLE standard' },
        rp2040: { name: 'RP2040', developer: 'Raspberry Pi', significance: 'Pi Pico chip' },
        teensy: { name: 'Teensy', significance: 'High-performance Arduino-compatible' }
    },
    singleBoardComputers: {
        raspberry_pi: { name: 'Raspberry Pi', year: 2012, significance: 'Most popular SBC', models: ['Pi 5', 'Pi 4', 'Pi Zero 2 W', 'Pi Pico'] },
        beaglebone: { name: 'BeagleBone', significance: 'Open hardware SBC' },
        nvidia_jetson: { name: 'NVIDIA Jetson', significance: 'AI/ML at the edge', models: ['Nano', 'TX2', 'Xavier', 'Orin'] },
        orange_pi: { name: 'Orange Pi', significance: 'Pi alternative' },
        rock_pi: { name: 'Rock Pi', developer: 'Radxa', significance: 'High-performance Pi alternative' }
    },
    rtos: {
        freertos: { name: 'FreeRTOS', year: 2003, significance: 'Most popular RTOS' },
        zephyr: { name: 'Zephyr', developer: 'Linux Foundation', significance: 'Modern IoT RTOS' },
        threadx: { name: 'Azure RTOS (ThreadX)', developer: 'Microsoft', significance: 'Billions deployed' },
        nuttx: { name: 'NuttX', significance: 'POSIX-compliant RTOS' },
        riot: { name: 'RIOT', significance: 'IoT OS' },
        mbed: { name: 'Mbed OS', developer: 'ARM', significance: 'ARM microcontroller OS' },
        contiki: { name: 'Contiki', significance: 'IoT pioneer' }
    },
    protocols: {
        i2c: { name: 'I2C', year: 1982, developer: 'Philips', significance: 'Serial communication bus' },
        spi: { name: 'SPI', significance: 'High-speed serial' },
        uart: { name: 'UART', significance: 'Serial communication' },
        can: { name: 'CAN Bus', year: 1986, developer: 'Bosch', significance: 'Automotive standard' },
        modbus: { name: 'Modbus', year: 1979, significance: 'Industrial automation' },
        zigbee: { name: 'Zigbee', significance: 'Low-power mesh networking' },
        lora: { name: 'LoRa', significance: 'Long-range IoT' },
        matter: { name: 'Matter', year: 2022, significance: 'Smart home standard' }
    },
    frameworks: {
        platformio: { name: 'PlatformIO', significance: 'Unified embedded development' },
        arduino_ide: { name: 'Arduino IDE', significance: 'Beginner-friendly' },
        esp_idf: { name: 'ESP-IDF', significance: 'Official Espressif framework' },
        stm32cube: { name: 'STM32CubeMX', significance: 'STM32 configuration' },
        micropython: { name: 'MicroPython', significance: 'Python for microcontrollers' },
        circuitpython: { name: 'CircuitPython', developer: 'Adafruit', significance: 'Beginner-friendly Python' },
        tinygo: { name: 'TinyGo', significance: 'Go for microcontrollers' },
        rust_embedded: { name: 'Embedded Rust', significance: 'Safe systems programming' }
    }
};

app.get('/api/embedded/categories', (c) => c.json({ success: true, categories: Object.keys(EMBEDDED_SYSTEMS) }));
app.get('/api/embedded/:cat', (c) => {
    const cat = c.req.param('cat') as keyof typeof EMBEDDED_SYSTEMS;
    return EMBEDDED_SYSTEMS[cat] ? c.json({ success: true, data: EMBEDDED_SYSTEMS[cat] }) : c.json({ error: 'Not found' }, 404);
});
app.get('/health', (c) => c.json({ status: 'healthy', worker: 'embedded-systems-worker' }));

export default app;
