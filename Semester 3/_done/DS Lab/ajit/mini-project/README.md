# AI Drawing Grader (CNN) 

A Streamlit mini‑project where a user **hears a random digit (0–9)** and draws it on a canvas. A CNN (trained on MNIST) then predicts the digit and uses the model’s confidence to generate a **score and feedback**.

> Main app: `src/app.py`  
> Model file: `drawing_grader_cnn.h5`

---

## Features

- Audio prompt for the target digit using **gTTS** (text‑to‑speech)
- In‑browser drawing canvas using **streamlit‑drawable‑canvas**
- Image preprocessing pipeline:
  - convert to grayscale → threshold → find contour → crop → resize to 20×20 → pad to 28×28
- CNN prediction + scoring logic (higher confidence → higher score)
- Debug section showing the exact 28×28 image the model “sees” + confidence bar chart

---

## Project Structure

- `src/app.py` — Streamlit UI for drawing, scoring, and debug visualization
- `src/train_model.py` — trains a CNN on MNIST and saves `drawing_grader_cnn.h5`
- `drawing_grader_cnn.h5` — pre-trained model used by the app
- `requirements.txt` — dependencies for the drawing grader app
- `new/` — separate Streamlit demo app (fashion style classifier; optional)

---

## Setup (Windows / PowerShell)

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the Drawing Grader App

```powershell
streamlit run src/app.py
```

The app expects `drawing_grader_cnn.h5` to be in the project root.

---

## Train / Re-train the Model (if needed)

If you don’t have the model file, or want to re-train it:

```powershell
python src/train_model.py
```

This trains a small CNN on the MNIST dataset and saves the model as `drawing_grader_cnn.h5`.

---

## Notes

- **gTTS requires an internet connection** to generate the audio prompt.
- First run of training may take a few minutes and will download MNIST automatically.

---

## Troubleshooting

- **“Error loading model”** in the app
  - Ensure `drawing_grader_cnn.h5` exists in the project root.
  - If missing, run `python src/train_model.py`.

- **Audio doesn’t play / gTTS errors**
  - Check your internet connection.
  - Some networks block Google TTS requests.

- **TensorFlow install issues on Windows**
  - Try a clean venv and reinstall dependencies.
  - If needed, install a specific TensorFlow version compatible with your Python.

---

## Optional: `new/` Fashion Style Demo

There is another Streamlit app under `new/` (`new/app.py`) that demonstrates a fashion style classifier UI.

This demo uses additional libraries **not listed** in `requirements.txt` (e.g., `pillow`, `pandas`, `plotly`, `scikit-learn`). If you want to run it, install them first, then:

```powershell
streamlit run new/app.py
```

---

## Tech Stack

- Python
- Streamlit
- TensorFlow / Keras
- OpenCV
- NumPy
- gTTS

