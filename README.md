# WeirdlyWired.CoreAPIs

## To run the local server
- Running local machine
```bash
run command: uvicorn weirdlywired.asgi:application --reload --debug
```

- Running at local network
```bash
daphne -b <local-network> -p 8000 --ping-interval 2 --ping-timeout 5 weirdlywired.asgi:application

# For eg
daphne -b 192.168.1.5 -p 8000 --ping-interval 2 --ping-timeout 5 weirdlywired.asgi:application

```