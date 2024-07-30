<div align="center">
  <img src="CTA.png" alt="Banner" style="border-radius: 17px; width: 100%; max-width: 800px; height: auto;">
</div>

<h3 align="center">
  <b><a href="https://pcb-lullaby.streamlit.app">Online App</a></b>
  •
  <b><a href="#python-api">Python API</a></b>
  •
  <b><a href="http://www.youtube.com/watch?v=_3DP3HD8CqY">Demo</a></b>
</h3>

<div align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python Versions">
</div>
</br>

<p align="center"><b>NonogramQR</b> is an innovative application that seamlessly integrates the challenge of nonograms with the functionality of QR codes. This app transforms your messages into engaging puzzles, providing a unique and interactive way to reveal hidden information.</p>

## How It Works

- **Message Encoding:** Enter your message or URL into the app or using the python API.
- **QR Code Generation:** The message is encoded into an hidden QR code.
- **Nonogram Creation:** The QR code is then converted into a nonogram pdf puzzle.
- **Puzzle Solving:** Solve the nonogram to reveal the QR code.
- **Scanning:** Use the app to scan the completed nonogram and access the original message or website.

## Features

- **Customizable Messages:** Encode any string of less than 25 caracter into a NonogramQR.
- **Puzzle Difficulty:** The complexity of the nonogram adjusts based on the length of the message.
- **Interactive Experience:** Engage with both puzzle-solving and QR code scanning in one seamless process.
- **User-Friendly Interface:** Simple and intuitive design for ease of use with online app.

## Run app locally
If you want to run the PCB Lullaby streamlit app locally. Two  solutions are possible:
1. **Run the app directly in a virtual environnement**
    
    clone repository:
    ```
    git clone https://github.com/azerty-labs/NonogramQR.git
    cd NonogramQR
    ```
    Create, activate and install your environnement:
    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
    Run the app using streamlit:
    ```
    streamlit run streamlit-app.py
    ```
2. **Run the app using docker**

    Build the `nonogram-qr` docker container:
    ```
    docker build -t nonogram-qr .
    ````
    Run the container at a specified port (here 8501) 
    ```
    docker run -p 8501:8501 nonogram-qr
    ```
    Go to your web browser and access [localhost:8501](http://localhost:8501)
  
## Python API

In order to use the NonogramQR code please do the following: 
```
git clone https://github.com/chloelavrat/NonogramQR.git
cd NonogramQR/
python -m venv venv
source ./venv/bin/activate
python pip install -r requirements.txt
python NonogramQR.py "My message to encode"
```
Then you can start using the code to generate your NonogramQR PDF.
```
$ python NonogramQR.py -h
usage: NonogramQR.py [-h] [--output OUTPUT] [message ...]

Convert a string into a QR code and then into a nonogram PDF.

positional arguments:
  message          Message to encode

options:
  -h, --help       show this help message and exit
  --output OUTPUT  Output PDF file name

Have fun!
```
## Contributing

The NonogramQR project is an open-source project, and contributions are always welcome. If you would like to contribute to the project, you can do so by submitting a pull request or by creating an issue on the project's GitHub page.

## License

The NonogramQR project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.