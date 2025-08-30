
# Flask + MongoDB Atlas Setup

Follow the steps below to set up and run the application (Backend + Frontend).

## Repository Link
[GitHub Repository](https://github.com/tejaskaher999/tutedude)


## MongoDB Atlas Connection String

Make sure to create and replace with your proper MongoDB Atlas URL:

```
MONGO_URI="mongodb+srv://<username>:<password>@cluster.houeyyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
```

## Setup Instructions

### 1. Check pip installation
```
pip --version
```

### 2. Create a virtual environment
```
virtualenv.exe env
```
Or
```
py -m venv env
```

### 3. Activate virtual environment
```
.\env\Scripts\activate.ps1
```

### 4. Navigate to backend folder
```
cd backend
```

### 5. Install dependencies
```
py -m pip install -r requirements.txt
```

### 6. Run the backend app
```
py app.py
```

---

## Frontend Setup

Open one more terminal.

### 1. Navigate to frontend folder
```
cd frontend
```

### 2. Activate virtual environment
```
..\env\Scripts\activate.ps1
```

### 3. Install dependencies
```
py -m pip install -r requirements.txt
```

### 4. Run the frontend app
```
py app.py
```
