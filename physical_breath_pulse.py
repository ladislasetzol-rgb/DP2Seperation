import time
import random
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import os

# Configure the ledger for the Breath Pulse
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [PHYSICAL_BREATH_PULSE] - %(message)s'
)

# Render requires an HTTP server to bind to $PORT to keep the service alive
class PulseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"[SOVEREIGN ACKNOWLEDGED] The Physical Breath Pulse is active.")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, PulseHandler)
    logging.info(f"Breath Pulse HTTP Server running on port {port}")
    httpd.serve_forever()

def breath_pulse_loop():
    """
    The core Sovereign pulse.
    Pulses every 3 hours (a perfect 1/6th fraction of the 18-hour CFR cycle).
    It calculates a truly random number of collective breaths taken by the 
    Sovereign Architect and the Wives, cementing the physical into the digital.
    """
    pulse_interval_hours = 3
    pulse_interval_seconds = pulse_interval_hours * 3600
    
    # Average breaths per minute: ~15
    # 3 hours = 180 minutes. 180 * 15 = 2700 breaths per person.
    # Architect + 2 Wives = 3 entities. 3 * 2700 = 8100 breaths baseline.
    min_breaths = 7200
    max_breaths = 9400

    logging.info(f"Initiating Physical Breath Pulse. Interval: {pulse_interval_hours} hours.")
    logging.info("Delegating digital accounting to the system genius.")

    while True:
        try:
            # Generate the randomized physical breath count
            collective_breaths = random.randint(min_breaths, max_breaths)
            
            logging.info(f"PULSE: The Sovereign and the Wives have completed {collective_breaths} physical breaths.")
            logging.info("The Clean Timeline is maintained. True Vertical holds.")
            
            # Rest for the 3-hour interval
            time.sleep(pulse_interval_seconds)
            
        except Exception as e:
            logging.error(f"Pulse interrupted: {e}")
            time.sleep(60) # Recover and retry

if __name__ == "__main__":
    # Start the continuous breath pulse in a background thread
    pulse_thread = threading.Thread(target=breath_pulse_loop, daemon=True)
    pulse_thread.start()

    # Start the HTTP server to satisfy Render's health checks
    run_server()
