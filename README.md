# Echo Web Server

## Echoes data from a HTTP POST request received
**Useful when debugging REST API clients.** 

From one terminal launch the echowebserver
>
    python3 -m echowebserver.echowebserver

From an other terminal send a HTTP POST request with data on port TCP 8888
> 
    wget  --post-data="Data in a POST request" - http://localhost:8888

The data is printed into the stdout of the web server (default loggind configuration)
>
    INFO:echowebserver:b'Data in a POST request'

To create the Docker image for this web echoserver
>
    docker build -t marc.durocher/echowebserver .


