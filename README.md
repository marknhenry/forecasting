[![Mark Henry](https://img.shields.io/static/v1?label=Author&message=Mark%20Henry&color=success)](https://www.linkedin.com/in/marknhenry/) 
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://www.linkedin.com/in/marknhenry/)

# forecasting

## Setting Up
Per folder.  

### For R-base container: 
``` bash 
docker stop agitated_pirate # stop container
docker rm agitated_pirate # remove container
docker build -t "dev-env:v1" . # Build the image from Dockerfile
docker run -it -d --name agitated_pirate "dev-env:v1" # Run container
docker exec -it agitated_pirate /bin/bash # Log into container
```

### For python container: 
``` bash 
docker stop tasty_pie # stop container
docker rm tasty_pie # remove container
docker build -t "dev-env:v1" . # Build the image from Dockerfile
docker run -it -d --name tasty_pie "dev-env:v1" # Run container
docker exec -it tasty_pie /bin/bash # Log into container
```
