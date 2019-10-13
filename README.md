# DevOps organizer service

## Preparing for launch
```
cp .env.example .env
docker-compose build
```

## Running tests
```
docker-compose run web py.test
```

## Running service
```
docker-compose up -d
```

## Sample request

``` 
POST http://172.104.135.190:8899/api/v1/organizer/distribute/
Content-Type: application/json

{
  "DM_capacity": 20,
  "DE_capacity": 8,
  "data_centers": [
    {
      "name": "Paris",
      "servers": 20
    },
    {
      "name": "Stockholm",
      "servers": 62
    }
  ]
}
```
Response:
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": {
    "DE": 8,
    "DM_data_center": "Paris"
  }
}
```