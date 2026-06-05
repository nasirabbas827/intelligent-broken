# intelligent_broken_final

## Overview
`intelligent_broken_final` is a lightweight Python web application that detects and repairs broken images using an AI‑driven approach. Users can upload a corrupted image through the web interface, and the system will generate a repaired version automatically.

## Features
- **Simple UI** – Upload a broken image via a clean HTML page (`templates/index.html`).
- **AI‑based restoration** – Leverages a pre‑trained model to reconstruct missing or damaged parts of an image.
- **File handling** – Stores original uploads in `static/uploads/` and repaired results in `static/repair/`.
- **Extensible architecture** – Core logic resides in `main.py`, making it easy to swap or upgrade the restoration model.

## Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3.x, Flask |
| Image Processing | Pillow, OpenCV (optional) |
| AI / ML | TensorFlow / PyTorch (model loading handled in `main.py`) |
| Front‑end | HTML5, CSS (static files) |
| IDE configuration | JetBrains IDE (`.idea/` folder) |

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/intelligent_broken_final.git
   cd intelligent_broken_final
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *If `requirements.txt` is not present, install the core packages manually:*
   ```bash
   pip install flask pillow
   # Add TensorFlow or PyTorch as required by your model
   ```

4. **(Optional) Set up API keys**
   - If the restoration model requires an external service, add the key to an environment variable:
     ```bash
     export REPAIR_API_KEY=YOUR_OWN_API_KEY
     ```

## Usage
1. **Start the Flask server**
   ```bash
   python main.py
   ```
   The application will run by default on `http://127.0.0.1:5000`.

2. **Open the web interface**
   - Navigate to `http://127.0.0.1:5000` in your browser.
   - Use the upload form to select a broken image (e.g., `static/uploads/br.jpg`).

3. **View results**
   - After processing, the repaired image will be saved to `static/repair/` (e.g., `br.jpg`) and displayed on the page.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for full terms.