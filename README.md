
# Potato Disease Classification using CNN

## 📌 Project Overview
This project is a **deep learning-based potato disease classification system** that identifies diseases in potato leaves using **Convolutional Neural Networks (CNNs)**. The system consists of:
- A **trained CNN model** built with **TensorFlow and Keras**, leveraging **data augmentation and preprocessing** techniques for improved accuracy.
- A **FastAPI backend** to serve predictions via API calls.
- A **frontend built with HTML and CSS**, providing a simple and interactive UI for users to upload images and receive predictions.
- The entire application is **deployed on Render**:
  - **Live App**: [Potato Classification Model](https://potato-classification-model-0oqc.onrender.com/)

---

## 🛠 Tech Stack

| Component  | Technology Used |
|------------|----------------|
| **Deep Learning** | TensorFlow, Keras |
| **Backend API** | FastAPI, Uvicorn |
| **Frontend** | HTML, CSS, Jinja2 |
| **Deployment** | Render |
| **Data Processing** | NumPy, Pillow |
| **Model Training** | CNN (Convolutional Neural Network) |

---

## 📂 Project Structure
The project follows a structured directory format to maintain clarity and modularity.

```
📂 Potato-Classification  
│── 📂 static/               # Frontend files (HTML, CSS)  
│── 📂 model/                # Trained CNN model  
│── 📂 data/                 # Dataset (if included)  
│── 📜 main.py               # FastAPI backend and model integration  
│── 📜 requirements.txt      # Dependencies list  
│── 📜 README.md             # Project documentation  
```

---

## 🚀 Features
✅ **Deep Learning-based Classification** using CNN.  
✅ **FastAPI for Backend API** to serve predictions efficiently.  
✅ **Interactive Web Interface** with HTML & CSS.  
✅ **Model Trained with Data Augmentation** for better generalization.  
✅ **API Documentation** available at `/docs`.  
✅ **Deployed on Render** for easy access.  

---

## 🔧 How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Kawaljeet999/POTATO-CLASSIFICATION
cd <POTATO-CLASSIFICATION>
```

### 2️⃣ Install Required Dependencies
Ensure you have Python **3.7+** installed, then run:
```bash
pip install -r requirement.txt
```

### 3️⃣ Run the FastAPI Server
Execute the following command to start the backend:
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT 
```

### 4️⃣ Open the Application in Browser
- Visit **`http://localhost:8000`** to access the web interface.
- API documentation available at **`http://localhost:8000/docs`**  

---

## 🖼️ Usage Instructions
1️⃣ Open the application in your browser.  
2️⃣ Upload an image of a potato leaf.  
3️⃣ The model will classify whether the leaf is **Healthy** or **Diseased**.  
4️⃣ The result will be displayed on the screen with a confidence score.  

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/` | Returns the home page |
| **POST** | `/predict` | Upload an image for classification |
| **GET** | `/docs` | API documentation (Swagger UI) |

---

## 📝 Future Improvements
🚀 **Enhance Model Accuracy** with more training data.  
🚀 **Add More Potato Diseases** for better classification.  
🚀 **Improve UI/UX** for a smoother experience.  
🚀 **Deploy with Docker** for better scalability.  

---

## 👨‍💻 Contributors
- **[Your Name]** - Developer & AI Engineer  

---

## 📜 License
This project is licensed under the **MIT License**.  
