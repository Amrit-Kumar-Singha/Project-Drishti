from threading import Thread
from gps_module import send_gps_data
from final import app
from audio import recognize_speech


def run_flask_app():
    app.run(host='0.0.0.0', port='5000', debug=False)

if __name__ == "__main__":
    # Create two threads, one for the Flask app and one for GPS data sending
    flask_thread = Thread(target=run_flask_app)
    gps_thread = Thread(target=send_gps_data)
    audio_thread=Thread(target=recognize_speech)

    # Start both threads
    flask_thread.start()
    gps_thread.start()
    audio_thread.start()

    # Wait for both threads to finish
    flask_thread.join()
    gps_thread.join()
    audio_thread.join()
