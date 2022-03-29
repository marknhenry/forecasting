[![Mark Henry](https://img.shields.io/static/v1?label=Author&message=Mark%20Henry&color=success)](https://www.linkedin.com/in/marknhenry/) 
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://www.linkedin.com/in/marknhenry/)

# forecasting

## Setting Up
Container has Jupyter with both Python and R

``` bash 
docker stop tasty_pie # stop container
docker rm tasty_pie # remove container
docker build -t "py-dev-env:v1" . # Build the image from Dockerfile
docker run -it -d --name tasty_pie "py-dev-env:v1" # Run container
docker exec -it tasty_pie /bin/bash # Log into container
```
