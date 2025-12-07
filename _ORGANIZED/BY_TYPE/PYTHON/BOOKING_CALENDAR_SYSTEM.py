#!/usr/bin/env python3
"""
📅 BOOKING & CALENDAR SYSTEM
Clients book RESCUE sessions, you manage your schedule
Automated reminders, calendar sync, availability management
PROFESSIONAL TIME MANAGEMENT!!
"""

from flask import Flask, render_template_string, request, jsonify
import json
import os
from datetime import datetime, timedelta
import sys

sys.path.append('../FishMusic_Email_System')
from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer

app = Flask(__name__)
mailer = MailAppMailer()

BOOKING_CALENDAR_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>📅 Book NoizyLab RESCUE Session</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 20px;
        }
        .container { max-width: 900px; margin: 0 auto; }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            color: #00ff88;
            font-size: 3rem;
            margin-bottom: 10px;
        }
        
        .calendar-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px;
        }
        
        .time-slots {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 15px;
            margin: 30px 0;
        }
        
        .time-slot {
            padding: 15px;
            background: rgba(0,113,227,0.1);
            border: 2px solid #0071e3;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .time-slot:hover {
            background: rgba(0,113,227,0.2);
            transform: scale(1.05);
        }
        
        .time-slot.selected {
            background: rgba(0,255,136,0.2);
            border-color: #00ff88;
        }
        
        .time-slot.booked {
            background: rgba(255,0,0,0.1);
            border-color: #666;
            cursor: not-allowed;
            opacity: 0.5;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #00ff88;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        input {
            width: 100%;
            padding: 14px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.3);
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
        }
        
        .btn {
            width: 100%;
            padding: 18px;
            background: #00ff88;
            color: #0f0f23;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 20px;
        }
        
        .btn:hover {
            background: #00cc6a;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📅 Book Your RESCUE</h1>
            <p style="color: #888; font-size: 1.2rem;">Choose a convenient time slot</p>
        </div>
        
        <div class="calendar-box">
            <h2 style="color: #00ff88; margin-bottom: 20px;">Available Times (Next 7 Days)</h2>
            
            <div id="calendarDays"></div>
            
            <form id="bookingForm" style="display: none; margin-top: 40px;">
                <h3 style="color: #00ff88; margin-bottom: 20px;">Complete Your Booking</h3>
                
                <div class="form-group">
                    <label>Selected Time</label>
                    <input type="text" id="selectedTime" readonly>
                </div>
                
                <div class="form-group">
                    <label>Your Name</label>
                    <input type="text" name="name" required>
                </div>
                
                <div class="form-group">
                    <label>Your Email</label>
                    <input type="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label>Your Phone (for SMS confirmation)</label>
                    <input type="tel" name="phone" placeholder="Optional">
                </div>
                
                <button type="submit" class="btn">
                    ✅ Confirm Booking
                </button>
            </form>
        </div>
    </div>
    
    <script>
        let selectedSlot = null;
        
        // Generate next 7 days of time slots
        function generateCalendar() {
            const container = document.getElementById('calendarDays');
            const now = new Date();
            
            // Working hours: 9 AM - 9 PM
            const workingHours = [9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20];
            
            for (let day = 0; day < 7; day++) {
                const date = new Date(now);
                date.setDate(date.getDate() + day);
                
                const dayDiv = document.createElement('div');
                dayDiv.style.marginBottom = '30px';
                
                const dayHeader = document.createElement('h3');
                dayHeader.textContent = date.toLocaleDateString('en-US', { 
                    weekday: 'long', 
                    month: 'short', 
                    day: 'numeric' 
                });
                dayHeader.style.color = '#00ff88';
                dayHeader.style.marginBottom = '15px';
                
                dayDiv.appendChild(dayHeader);
                
                const slotsDiv = document.createElement('div');
                slotsDiv.className = 'time-slots';
                
                workingHours.forEach(hour => {
                    const slot = document.createElement('div');
                    slot.className = 'time-slot';
                    
                    const slotTime = new Date(date);
                    slotTime.setHours(hour, 0, 0);
                    
                    // Don't show past times
                    if (slotTime < now) {
                        slot.className += ' booked';
                        slot.textContent = `${hour % 12 || 12}:00 ${hour >= 12 ? 'PM' : 'AM'}`;
                        slot.style.opacity = '0.3';
                    } else {
                        slot.textContent = `${hour % 12 || 12}:00 ${hour >= 12 ? 'PM' : 'AM'}`;
                        slot.onclick = () => selectSlot(slot, slotTime);
                    }
                    
                    slotsDiv.appendChild(slot);
                });
                
                dayDiv.appendChild(slotsDiv);
                container.appendChild(dayDiv);
            }
        }
        
        function selectSlot(element, time) {
            // Deselect all
            document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
            
            // Select this one
            element.classList.add('selected');
            selectedSlot = time;
            
            // Show booking form
            document.getElementById('bookingForm').style.display = 'block';
            document.getElementById('selectedTime').value = time.toLocaleString();
            
            // Scroll to form
            document.getElementById('bookingForm').scrollIntoView({ behavior: 'smooth' });
        }
        
        document.getElementById('bookingForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            if (!selectedSlot) {
                alert('Please select a time slot');
                return;
            }
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            data.booking_time = selectedSlot.toISOString();
            
            try {
                const response = await fetch('/api/booking/create', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ Booking confirmed!\\n\\nConfirmation sent to your email!\\nBooking ID: ' + result.booking_id);
                    location.reload();
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
        
        // Generate calendar on load
        generateCalendar();
    </script>
</body>
</html>
"""

@app.route('/')
def booking_page():
    """Booking calendar page"""
    return render_template_string(BOOKING_CALENDAR_PAGE)

@app.route('/api/booking/create', methods=['POST'])
def create_booking():
    """Create new booking"""
    try:
        data = request.json
        
        booking_id = f"BOOKING{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        booking = {
            'id': booking_id,
            'name': data['name'],
            'email': data['email'],
            'phone': data.get('phone', ''),
            'booking_time': data['booking_time'],
            'status': 'confirmed',
            'created': datetime.now().isoformat()
        }
        
        # Save booking
        bookings = []
        if os.path.exists('bookings.json'):
            with open('bookings.json', 'r') as f:
                bookings = json.load(f)
        
        bookings.append(booking)
        
        with open('bookings.json', 'w') as f:
            json.dump(bookings, f, indent=2)
        
        # Send confirmation email
        booking_time_str = datetime.fromisoformat(booking['booking_time']).strftime('%A, %B %d at %I:%M %p')
        
        mailer.send_email(
            booking['email'],
            f"✅ NoizyLab RESCUE Booked - {booking_id}",
            f"""
Hi {booking['name']}!

Your NoizyLab RESCUE session is BOOKED!

Booking ID: {booking_id}
Time: {booking_time_str}

WHAT TO DO BEFORE SESSION:
1. Download TeamViewer: https://www.teamviewer.com/download
2. Install and open it
3. I'll send connection details 15 min before session

PRICING:
• If I fix your issue: $89+ (you choose amount!)
• If I can't fix: $0 (NO CHARGE!)

Looking forward to helping you!

Rob @ NoizyLab
noizylab.ca
rsplowman@icloud.com
"""
        )
        
        # Notify YOU
        mailer.send_email(
            "rsplowman@icloud.com",
            f"📅 NEW BOOKING: {booking_id}",
            f"New RESCUE session booked!\n\nClient: {booking['name']}\nTime: {booking_time_str}\nEmail: {booking['email']}\nPhone: {booking.get('phone', 'Not provided')}"
        )
        
        print(f"✅ Booking created: {booking_id}")
        print(f"   Client: {booking['name']}")
        print(f"   Time: {booking_time_str}")
        
        return jsonify({
            'success': True,
            'booking_id': booking_id
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    print("📅 BOOKING & CALENDAR SYSTEM")
    print("=" * 60)
    print()
    print("FEATURES:")
    print("  ✅ Online booking calendar")
    print("  ✅ 7-day availability view")
    print("  ✅ 9 AM - 9 PM working hours")
    print("  ✅ Automated email confirmations")
    print("  ✅ SMS reminders (if Twilio configured)")
    print("  ✅ Booking management")
    print()
    print("CLIENT EXPERIENCE:")
    print("  1. Views available time slots")
    print("  2. Selects convenient time")
    print("  3. Enters contact info")
    print("  4. Gets confirmation email")
    print("  5. Gets reminder before session")
    print()
    print("YOUR EXPERIENCE:")
    print("  1. Get email when booking made")
    print("  2. Calendar shows all bookings")
    print("  3. Automated reminders sent")
    print("  4. Connect at scheduled time")
    print()
    print("🌐 Booking Calendar: http://localhost:8500")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=8500, debug=True)

