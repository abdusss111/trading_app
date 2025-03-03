# 🚀 Trading App (Django + Daphne + Celery + Redis )

##link to video - https://www.youtube.com/watch?v=w-KN1kh_ga8 ##

A real-time trading platform built with **Django**, **Daphne**, **Celery**, and **WebSockets**. This application supports user authentication, real-time order execution, invoice generation, and automated analytics reporting.

## 📌 Features

✅ **User Roles**: Admin, Traders, Sales Representatives, Customers  
✅ **Real-time Trading**: WebSockets for instant order updates  
✅ **Sales & Invoicing**: Automated invoice generation  
✅ **Analytics Reports**: Data-driven insights for trades and sales  
✅ **Background Tasks**: Celery & Redis for notifications and reports  
✅ **REST API**: Fully documented with **Swagger (drf-yasg)**  

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/trading-app.git
cd trading-app
```

### **2️⃣ Create Environment Variables**
Create a `.env` file in the project root:
```ini
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@postgres_db:5432/postgres
REDIS_URL=redis://redis_cache:6379/0
```

### **3️⃣ Build & Start the Application**
```bash
docker-compose up --build
```
🚀 The app will be available at: **http://127.0.0.1:8000**

---

## 📡 WebSockets (Real-time Trading)

- **Live trading updates** are handled using **Daphne** and **Django Channels**.
- **WebSocket Endpoint**: `ws://127.0.0.1:8000/ws/trading/`
- Example **JavaScript WebSocket Client**:
```javascript
let socket = new WebSocket("ws://127.0.0.1:8000/ws/trading/");
socket.onmessage = (event) => console.log("Received:", event.data);
socket.onopen = () => socket.send(JSON.stringify({"action": "place_order", "order_id": 123}));
```

---

## 📊 API Documentation

### **Swagger UI**  
🔗 [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

### **Redoc UI**  
🔗 [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### **Example Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/users/register/` | Register a new user |
| **POST** | `/users/login/` | Authenticate user |
| **GET** | `/trading/orders/` | Get all orders |
| **POST** | `/trading/orders/` | Place a new trade |
| **GET** | `/analytics/report/` | Fetch analytics report |
| **GET** | `/sales/invoices/` | Retrieve invoices |

---

## ✅ Running Migrations & Seeding Data

1. **Run Database Migrations**
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

2. **Generate Test Data**
```bash
docker-compose exec web python manage.py generate_test_data
```

---

## 🧪 Testing API Endpoints (cURL)

```bash
# Test User Registration
curl -X POST http://127.0.0.1:8000/users/register/ -d "username=test&password=123456"

# Test WebSocket Connection (Using wscat)
wscat -c ws://127.0.0.1:8000/ws/trading/
```

---

## 🛑 Stopping the Application
```bash
docker-compose down
```

---

## 🏗️ Built With

- **Django 5.1** (Backend)
- **Daphne & Django Channels** (WebSockets)
- **Celery & Redis** (Background Tasks)
- **PostgreSQL** (Database)
- **Docker & Docker Compose** (Deployment)


