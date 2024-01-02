# gps_module.py
import serial
import time
import pyrebase
import pynmea2

def send_gps_data():
    firebaseconfig = {
        "apiKey": "AIzaSyBE9Sv-C4mSO1ZeyPLl8uv59qExaPNJLj4",
        "authDomain": "drishti-ab653.firebaseapp.com",
        "databaseURL": "https://drishti-ab653-default-rtdb.firebaseio.com",
        "projectId": "drishti-ab653",
        "storageBucket": "drishti-ab653.appspot.com",
        "messagingSenderId": "495917202335",
        "appId": "1:495917202335:web:47b9f422b86e8ee1939baa",
    }

    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    while True:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.1)
        dataout = pynmea2.NMEAStreamReader()

        try:
            newdata = ser.readline().decode('unicode_escape')
            if newdata[0:6] == "$GPRMC" and newdata.count(',') == 12:
                newmsg = pynmea2.parse(newdata)
                lat = newmsg.latitude
                lng = newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                data = {"LAT": lat, "LNG": lng}
                if lat != 0 and lng != 0:
                    db.update(data)
                    print("data sent")
                else:
                    print(gps)
            else:
                print("Invalid or incomplete NMEA sentence:", newdata)
        except serial.SerialException as e:
            print(f"SerialException: {e}")
            # Handle the exception here, such as logging the error or taking other actions
        except pynmea2.ParseError as e:
            print(f"ParseError: {e}")
            # Handle the exception here, such as logging the error or taking other actions
        finally:
            ser.close()  # Close the serial port when done

        # Optional: Sleep for a short duration to control the rate of reading data
        time.sleep(0.1)  # Sleep for 1 second between readings

if __name__ == "__main__":
    # This block will only be executed if the script is run directly, not when it's imported as a module
    send_gps_data()
