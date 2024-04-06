# QR Code Generator

This web application built with HTML, Tailwind CSS, JavaScript, and Flask allows you to convert entered website links or any text into QR codes instantly.

## Features

- Convert any URL or text into a QR code.
- Easy-to-use interface with real-time QR code generation.

## How to Use

1. **Enter Your Content**: In the input field on the homepage, type the website URL or text that you want to convert into a QR code.
2. **Generate QR Code**: Click the "Generate QR Code" button.
3. **View and Download**: Once the QR code is generated, it will appear on the screen. You can download the QR code image using the download button.

## Installation and Setup

To run this project locally, follow these steps:

### Prerequisites

- Python (3.6 or higher)
- Flask

## Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

## Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

## Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```

##Run the Application
```bash
Copy code
flask run
```

## Project Structure

- `app.py`: Flask application file.
- `templates/`: HTML templates (Tailwind CSS) for the web application.
- `static/`: Contains CSS, JavaScript and Image files.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or a pull request.
