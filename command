docker build -t my-fastapi-app
docker-compose up --build
docker run -p 8000:8000 my-fastapi-app
docker-compose exec fastapi poetry run pip list