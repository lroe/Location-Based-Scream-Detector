from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os
from datetime import datetime
import wave

from joblib import load
import numpy as np
import librosa

# Function to extract audio features
def extract_features(y, sr, mfcc=True, chroma=True, mel=True):
    features = []
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
        features.extend(mfccs)
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
        features.extend(chroma)
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr).T, axis=0)
        features.extend(mel)
    return np.array(features).reshape(1, -1)

# Load the trained SVM model
model_file = 'svm_model.joblib'
print("Loading the trained SVM model...")
svm_classifier = load(model_file)
print("Model loaded successfully.")

app = Flask(__name__, static_folder='audios')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio_from_client')
def handle_audio_from_client(data):  # Receive both audio data and client info
    audio_data = data['audio_data']
    client_name = data['client_name']
    x_coordinate = data['x']
    y_coordinate = data['y']
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the directory if it doesn't exist
    os.makedirs(app.static_folder, exist_ok=True)
    
    file_path = os.path.join(app.static_folder, f"{timestamp}.wav")
    
    # Write audio data to a WAV file
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)  # Assuming mono audio
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(44100)  # Sample rate
        wf.writeframes(audio_data)
    
    print('Audio clip received from client', client_name + '. Saved as:', file_path)
    
    y, sr = librosa.load(file_path)
    features = extract_features(y, sr)

    # Predict using the SVM model
    prediction = svm_classifier.predict(features)[0]

    # Print the prediction
    if prediction == 1:
        print("Prediction: Scream")
        # Emit message to client along with audio path, client name, and coordinates
        socketio.emit('scream_detected', {'time': timestamp, 'audioURL': f'audios/{timestamp}.wav', 'client_name': client_name, 'x': x_coordinate, 'y': y_coordinate})
    else:
        print("Prediction: Not a Scream")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print("Starting the server...")
    socketio.run(app, debug=True, port=4023, use_reloader=False)
    print("Server is running on http://127.0.0.1:4023/")
