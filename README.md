# Flask-Swagger-Image-Classification-API
* This project aims to classify a given image as ***Cat/Dog***. The image is posted to the server via OpenAPI protocol.

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
```
There will be a table like below.

| REPOSITORY      | TAG | IMAGE ID | CREATED | SIZE|
| ----------- | ----------- | ----------- | ----------- | ----------- |
| flask-swagger-cat-dog-classification-tensorflow-api      | latest | 2bcc97f67db1 | 31 minutes ago | 1.81GB |

Get the ```IMAGE ID``` and paste it below.
```bash
$ docker run -it -p5000:5000 'IMAGE-ID'
```

Then open your browser and type `localhost:5000/ui` for swagger UI.

## TODO
- [x] Implementing the Flask Server
- [x] Implementing the image classifier
- [x] Creating test file.
- [x] Dockerize the project.
