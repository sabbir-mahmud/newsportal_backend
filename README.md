# 📰 New Portal API

A **Python Django**-based backend application for a news portal. It retrieves the latest news every **10 minutes** using [NewsAPI.org](https://newsapi.org/).

---

## 🚀 Project Setup

### ✅ 1. Set up Virtual Environment

```bash
python -m venv venv
```

### ✅ 2. Activate Virtual Environment

* **Linux/macOS:**

```bash
source venv/bin/activate
```

* **Windows:**

```bash
venv\Scripts\activate
```

### ✅ 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### ✅ 4. Configure Environment Variables

Create a `.env` file in the project root.
Use `.env.sample` as a reference for required variables.

### ✅ 5. Apply Migrations

```bash
python manage.py migrate
```

### ✅ 6. Load Initial Data

```bash
python manage.py loaddata ./pg_data.json
```

> 💡 You can use the full path if needed.

### ✅ 7. Run Django Development Server

```bash
python manage.py runserver
```

### ✅ 8. Start Celery Services

* **Celery Beat Scheduler:**

```bash
celery -A news beat -l INFO
```

* **Celery Worker:**

```bash
celery -A news worker --loglevel=info
```

---

## 📘 Documentation & Postman Collections

### 🔗 DRF Generated Docs

Access API documentation at:

```
http://127.0.0.1:8000/api/docs/
```

### 📦 Postman Collections

* **Collection file:** `news api.postman_collection.json`
* **Environment file:** `news local.postman_environment.json`

> 📁 Both files are located at the **root of the project**.

---

## 🌐 Links

* [NewsAPI Documentation](https://newsapi.org/docs)

---

## 📄 License

This project is licensed under the **MIT License**.

---