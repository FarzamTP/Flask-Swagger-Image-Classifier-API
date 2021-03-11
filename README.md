# Flask-Swagger-Image-Classification-API
* This project aims to get an image's url as a request, and classify the image to return the result to user via OpenAPI protocols.

## How to run
### Wihhout Docker Image 
```bash
$ git clone https://github.com/FarzamTP/Flask-Swagger-Image-Classifier-API.git
$ cd Flask-Swagger-Image-Classifier-API
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ chmod +x app.py
$ ./app.py
```

### Wih Docker Image 
```bash
$ docker pull farzamtp/flask-swagger-cat-dog-classification-tensorflow-api:latest 
$ docker images
# Get the images's ID!
# | REPOSITORY      | TAG | IMAGE ID | CREATED | SIZE|
# | ----------- | ----------- | ----------- | ----------- | ----------- |
# | farzamtp/flask-swagger-cat-dog-classification-tensorflow-api      | latest | 2bcc97f67db1 | 31 minutes ago | 1.81GB |
$ docker run -it -p5000:5000 $(image_id)
```

Then open your browser and type `localhost:5000/ui` for swagger UI.

## TODO
- [x] Implementing the Flask Server
- [x] Implementing the image classifier
- [x] Creating test file.
- [x] Dockerize the project.