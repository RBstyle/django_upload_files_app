# django_upload_files_app
Simple dockerized uploading files app with Django REST framework

### Requirements:

1. docker-compose v2.22.0 (https://github.com/docker/compose/releases)
 
### RUN
1. Clone project
```bash
$ git clone git@github.com:RBstyle/django_upload_files_app.git
$ cd django_upload_files_app
```
2. Rename "env" file
```bash
$ mv example.env .env
```
3. Run project
```
$ docker-compose up --build
```

### Usage
## example 1 (text file)
```bash
$ curl -F "file=@123.txt" http://0.0.0.0:8000/upload/
{
"id": 1,
"file": "/uploads/123_212217.txt",
"uploaded_at": "2023-09-26T21:22:28.029990Z",
"processed": false
  }


```
in docker console "processing text" message if text file uploaded( formats available: text, image, video, audio)
```docker
celery_1  | [2023-09-26 21:22:18,006: WARNING/ForkPoolWorker-2] processing text file ID:1
... 10sec ...
celery_1  | [2023-09-26 21:22:28,061: WARNING/ForkPoolWorker-2] Done! File ID:1

```
after 10 sec
```bash
$ curl http://0.0.0.0:8000/files/
[
  {
    "id": 1,
    "file": "/uploads/123_212217.txt",
    "uploaded_at": "2023-09-26T21:22:28.029990Z",
    "processed": true
  }
]

```
## example 1 (image file)
```bash
curl -F "file=@222.png" http://0.0.0.0:8000/upload/
{
    "id": 2,
    "file": "/uploads/222_212712.png",
    "uploaded_at": "2023-09-26T21:27:12.737265Z",
    "processed": false
  }



```
in docker console "processing image" message if image file uploaded( formats available: text, image, video, audio)

```docker
celery_1  | [2023-09-26 21:27:12,760: WARNING/ForkPoolWorker-2] processing image file ID:2

... 10sec ...
celery_1  | [2023-09-26 21:27:23,058: WARNING/ForkPoolWorker-2] Done! File ID:2


```
after 10 sec
```bash
$ curl http://0.0.0.0:8000/files/
[
  {
    "id": 1,
    "file": "/uploads/123_212217.txt",
    "uploaded_at": "2023-09-26T21:22:28.029990Z",
    "processed": true
  },
  {
    "id": 2,
    "file": "/uploads/222_212712.png",
    "uploaded_at": "2023-09-26T21:27:22.777030Z",
    "processed": true
  }
]

```
