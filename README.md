# 🎵 InstaTune AI — Bollywood Song Recommender

AI-powered web app that recommends the most suitable **Bollywood songs** based on uploaded images, keywords, and user mood.

Built with **FastAPI + Streamlit + Google Gemini 3 Flash (Multimodal)**, InstaTune AI analyzes visual emotion and context to generate smart music recommendations for Instagram posts and stories.

---

## ✨ Features

* 🖼️ Upload up to 5 images
* 🧠 Emotion detection from images
* 🔍 Keyword-based refinement
* ⏱️ Duration filtering
* 🎧 Bollywood song recommendations
* ⚡ FastAPI backend
* 🎨 Streamlit interactive UI
* 🔄 Auto-reload during development

---

## 🏗️ Project Structure

```
InstaTune AI/
│
├── app.py               # Streamlit frontend
├── api.py               # FastAPI backend
├── recommender.py       # Song recommendation engine
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🚀 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Streamlit**
* **Uvicorn**
* **Google Gemini 3 Flash (Multimodal)**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/instatune-ai.git
cd instatune-ai
```

---

### 2️⃣ Create virtual environment (recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🔹 Start FastAPI backend

```bash
uvicorn api:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

### 🔹 Start Streamlit frontend (new terminal)

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User uploads images
2. Emotion model analyzes visual mood
3. Keywords refine the context
4. Recommendation engine filters songs
5. Best Bollywood songs are returned

---

## 📸 Future Improvements

* 🎯 Better emotion accuracy
* 🌍 Multi-language songs
* 🎵 Spotify integration
* 🤖 Deep learning upgrade
* ☁️ Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is for educational and portfolio purposes.

---

## 👩‍💻 Author

**Rutu Dave**

* 🌐 Aspiring AI/ML Developer
* 🇨🇦 Based in Canada
* 🎓 Passionate about AI-powered applications

---

⭐ If you like this project, don't forget to **star the repo**!
