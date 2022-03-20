# FastAPI Users CRUD

## Running

```
git clone https://github.com/KhirilovA/fastapi_users
```
```
pip install -r requirements.txt
```

Create your PostgreSQL Database

Put the data into .env file and docker-compose.yml "environment:"

### Create users table
```
python create_db.py
```

### Run the api
```
uvicorn main:app
```
