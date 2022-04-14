[![Mark Henry](https://img.shields.io/static/v1?label=Author&message=Mark%20Henry&color=success)](https://www.linkedin.com/in/marknhenry/) 
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://www.linkedin.com/in/marknhenry/)

# forecasting using Databricks

## Setting Up
Container has Jupyter with both Python

``` bash 
docker stop brick_pie # stop container
docker rm brick_pie # remove container
docker build -t "forecast-dev-env:v2-databricks" . # Build the image from Dockerfile
docker run -it -d --name brick_pie "forecast-dev-env:v2-databricks" # Run container
docker exec -it brick_pie /bin/bash # Log into container
```

# Github Actions
## On Azure CLI: 
az ad sp create-for-rbac --name "GHCICD" --role contributor --scopes /subscriptions/{subscription_id} --sdk-auth

## Add results in Github Action Secret Called **AZURE_CREDENTIALS_NORG** (NORG: No Resource Group)