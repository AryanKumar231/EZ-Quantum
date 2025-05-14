# EZ Quantum 🎓📁

**EZ Quantum** is a Django Rest Framework (DRF)-based backend project built for secure file handling. It supports:

- 📤 File upload by "Operation Users"
- 📥 File download by "Client Users"
- 🔐 Role-based permissions
- ✅ Postman-tested API endpoints

> This project helps organize and distribute assignments or documents between two user roles: Operators and Clients.

---

## 🚀 Live Demo (EZ Team please understand it. I am using Mailtrap to send email but Mailtrap charges money for forwarding email so I am showing you a demo)
you can follow this link for demo https://drive.google.com/file/d/1ngLP9U4exiW2n3leFtvnKkCw1BWHchDQ/view?usp=sharing

#Users
-operation-user
  -email: abc@abc.com
  -pass: 1234

-client-user
  -email:aryankashyap03873@gmail.com
  -pass:12345


### 🔗 API Test Collection:
You can also test the api endpoints on postman with give postman json file

## 🛠️ Features

- Role-based upload/download functionality
- Secure file handling using Django 5+ and DRF
- UUID-based Assignment ID
- File types restricted to `.pptx`, `.docx`, and `.xlsx`
- User authentication using DRF Token Auth / JWT
- Admin panel for file and user management
- Media storage support

---

## 📁 Folder Structure

EZ-Quantum/
├── eztest/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── ezfiles/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── users/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── media/
│ └── uploads/
├── .env
├── requirements.txt
└── README.md


---

## 📌 API Endpoints

### 🔐 Auth

- `POST /api/users/register` – Register user
- `POST /api/users/login/` – Login User

### 📤 File Upload (Operation User only)

```http
POST /api/files/
Headers: Authorization: Bearer <token>
Body: Multipart form (file=<your file>)
```
##Request
GET /api/files/download-file/<assignment_uuid>/
Headers: Authorization: Bearer <token>

##Response
{
  "download_link": "http://localhost:8000/media/uploads/<uuid>",
  "message": "success"
}


#Installation guide
git clone https://github.com/AryanKumar231/EZ-Quantum.git
cd EZ-Quantum
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
cp .env.example .env  # create your .env file and fill values
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
