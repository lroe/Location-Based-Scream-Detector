# Location-Based-Scream-Detector (Miniproject - Semester 6)

Developed by  Clerine Maria Ignatious & Jeevan Kumar M S

A real-time scream detection system using TCP multi-client server communication, SVM for audio classification, and geolocation mapping to visualize detected screams.

The server processes the audio using a Support Vector Machine (SVM) algorithm to detect screams. When a scream is detected, the system logs the location of the event on a map, providing a visual representation of recent scream occurrences along with their geotagged locations.

Features:
TCP Multi-client Server: Multiple microphones (clients) can send audio data to the server concurrently for processing, enabling real-time scream detection from multiple locations.

Real-time audio processing: Microphones capture and transmit audio to the server, where it is analyzed for screams.
Scream detection using SVM: The server uses a Support Vector Machine (SVM) algorithm to classify audio data and identify scream-like sounds.

Location-based mapping: Each detected scream is linked to a specific location and displayed on a map.

Web-based visualization: A user-friendly web interface shows recent scream events with their geotagged locations on an interactive map.
Technologies Used:

Python: Backend audio processing, server implementation, and SVM algorithm.

TCP/IP: Multi-client server communication for concurrent audio data processing.
Support Vector Machine (SVM): For classifying audio signals and detecting screams.

Flask: Web framework for creating the map-based user interface.

JavaScript (Leaflet.js): For displaying geotagged scream events on an interactive map.

# Screenshots
<img src="https://github.com/lroe/Location-Based-Scream-Detector/blob/main/Screenshot%20from%202024-07-07%2014-56-39.png">

<img src="https://github.com/lroe/Location-Based-Scream-Detector/blob/main/Screenshot%20from%202024-07-07%2014-56-40.png">
(a red light showing recently scream detected area)

# HOW TO USE
*create folder templates and copy 3.jpg and index.html there
1) python app.py -->click on the url to open the website
2) python client.py
3) play the audio on phone
