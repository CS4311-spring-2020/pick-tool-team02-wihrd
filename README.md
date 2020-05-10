# pick-tool-team02-wihrd
This project is dedicated to building the PMR(Prevent,Mitigate,Recover) Insignt Collective Knowledge System Tool which is focused on assisting teams doing cyber attack analysis within the ARL's cyber security and defense team. 


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. Each Component has their own installation requirements and dependencies.


## General System
We require the following throughout all components within the system

### Prerequisites 
This system requires Python 3.7 or Newer

### Dependencies
This Project uses pyqt5 and splunk for all GUI and Splunk related activities

To install pyqt5 run the following
```
pip install PyQt5
```
To install splunk do the following
1. Install the splunk sdk by running the following
  ```
  pip install splunk-sdk
  ```
2. Download and make an account with splunk from https://www.splunk.com/
3. Run the local splunk server and setup your username and password
4. Change the username, password, and port numbers in the splunkAuth.py file to what you configured in your splunk installation

### Deployment
The Following outlines the steps required to run the system

1. Setup and run the splunk local server by running the splunk application dowloanded above
2. Run the HomePage.py file found in the PICK_1.0/src/UI/ folder by running the followng in the terminal
```
python HomePage.py
```

## Optical Character Recognition(OCR) and Transcription Module
This module focuses on translating Image and Audio/Visual files into text files for File Ingestion for Splunk

### Prerequisites 
This module requries Python 3 and PyQT5

### Dependencies 
This module has two sets of dependencies, one for the OCR and one for the Transcription Module 

#### OCR
The OCR component uses PyTesseract, Tesseract, and pillow. You can install them by doing the following:

* PyTesseract: Run the following in your terminal:
```
  pip install pytesseract
```
* Tesseract: Run the following in your terminal:
```
  pip install tesseract
```
* pillow: Run the following in your terminal:
```
  pip install pillow
```

#### Transcription
The Transcription component uses pydub, AudioSegment, ffmpeg. You can install them by doing the following:

* pydub: Run the following in your terminal:
```
  pip install pydub
```
* AudioSegment: Run the following in your terminal:
```
  pip install audiosegment
```
* ffmpeg: Install the following path variable by doing the following:
  1. Download ffmpeg library from https://ffmpeg.zeranoe.com/builds/
  2. Unzip the folder and move it to the C drive 
  3. Add the file path to the extracted folder to the Enviorment variables/Path Variable
  
### Deployment
* OCR:
  1. Specify the filepath for the file you wish to convert in the im variable in the OCR.py File 
  2. Run the following in the terminal
    ```
    python OCR.py
    ```
* Transcription:
  1. Specify the filepath for the file you wish to convert in the filepath variable in the Transcriber.py File
  2. Run the following in the terminal
    ```
    python Transcriber.py
    ```


## Graph Module
This module is for managing the graph and all subsequent node/connector relations 

### Prerequisites
This module requires Python 3 and PyQt5

### Dependencies
This module uses QGraphViz 

To install QGraphViz run the following in your terminal
```
  pip install QGraphViz
```

### Deployment 
To Run this module move to the PICK_1.0/src/UI/QGraphView directory and run the following in your terminal 
```
  python QGraphViewer.py
```

## And Thats All You Need To Run PICK

## Quick Notes
* This system is designed to ingest files marked in three directories: White, Red, and Blue
* All dates in this system are handled in ZULU time
* This system is designed to handle .txt, .xlsx, and .csv files
* The graph only exports to .json files




