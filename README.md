# Project-Drishti

## Problem Statement-
In crowded events such as fairs, carnivals, and festivals, the presence of police personnel is

crucial for effective crowd control and ensuring the safety of attendees. These events often
require a well-organized deployment strategy where specific officers are assigned to particular
spots to manage and monitor the crowd efficiently. However, it has come to attention that on
numerous occasions, designated personnel have abandoned their assigned positions and ventured
into areas lacking surveillance or oversight. To address this issue, our primary objective is to
implement a comprehensive tracking and monitoring system that not only identifies instances of
personnel leaving their designated posts but also provides insights into their activities during
their absence from these critical locations. This approach is essential for maintaining a secure
environment and ensuring that officers remain committed to their assigned duties.

Methodology-
Tools needed (hardware)-

1. Raspberry Pi 4 model B (4GB RAM)
2. U-Blox Neo-6M GPS Module
3. Mini USB Microphone 2.0 (for Raspberry Pi)
4. RF-ID RC522 Tags
5. PiCam (optional)
Tools needed (software)-
1. Folium (python)
2. SpeechRecognition API (python)
3. PyAudio (python)
4. Flac Library (python)
5. Raspbian OS
6. MongoDB/FireBase Database
7. Jupyter Notebook/ VS Code
Step-1: Geo-Fencing:
The U-Blox Neo-6M GPS Module will provide Raspberry Pi with real-time GPS Coordinates of
the User carrying the device. The Geo-Fencing algorithm will keep a constant track of the Users
GPS coordinates, whether he/she is there in their predefined designated area or not.
Step-2: Map Generation:
The GPS coordinates collected by the U-Blox Neo-6M GPS Module will be sent to a MongoDB
or Firebase Database for storage. To visualize these coordinates in real-time, we will use the
Folium library in Python. Another device, acting as a display, will retrieve the GPS coordinates
from the database and render real-time maps for the user to view.
Step-3: Real-Time Speech-to-Text:
To enhance user interaction, the system will utilize the SpeechRecognition API in Python, along
with PyAudio for audio recording and the Flac Library for audio format conversion. A Mini USB
Microphone 2.0 connected to the Raspberry Pi will capture real-time speech and convert it into
text data. If the user happens to leave the predefined area for a specified period, this data will be
pushed to the MongoDB or Firebase Database, allowing for further analysis and tracking.
