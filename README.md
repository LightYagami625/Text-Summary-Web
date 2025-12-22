# AI Text Summarizer 🚀

A modern, web-based AI Text Summarization application that uses state-of-the-art Natural Language Processing (NLP) models to transform long articles into concise, readable summaries.

![AI Summarizer Demo](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-black)

## ✨ Features

- **Instant Summarization**: Powered by the `sshleifer/distilbart-cnn-12-6` model for high-quality extraction and abstraction.
- **Customizable Length**: Choose between **Concise**, **Balanced**, and **Detailed** summary modes.
- **Real-time Metrics**:
    - **Word Count**: Tracks input and output word counts as you type or generate.
    - **Readability Score**: Calculates the **Flesch Reading Ease** score to help you understand the complexity of your text.
- **Modern UI**: A premium, dark-themed interface with glassmorphism effects and smooth transitions.
- **Streaming Response**: Summaries are streamed in real-time, providing immediate visual feedback.

## 🛠️ Technologies

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **AI/ML**: [Hugging Face Transformers](https://huggingface.co/transformers/) (DistilBART)
- **Frontend**: Vanilla HTML5, CSS3, and JavaScript
- **Styling**: Modern CSS with CSS Variables and Flexbox

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LightYagami625/Text-Summary-Web.git
   cd Text-Summary-Web
   ```

2. **Create a virtual environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📈 Readability Scoring

The application uses the **Flesch Reading Ease** formula:
`Score = 206.835 - 1.015 * (Total Words / Total Sentences) - 84.6 * (Total Syllables / Total Words)`

- **90-100**: Very Easy (5th grade level)
- **60-70**: Standard (8th-9th grade level)
- **0-30**: Very Difficult (Professional/Academic)

---

Developed with ❤️ by **Nerd-SWAYAM**
