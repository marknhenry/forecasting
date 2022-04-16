[![Mark Henry](https://img.shields.io/static/v1?label=Author&message=Mark%20Henry&color=success)](https://www.linkedin.com/in/marknhenry/) 
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://www.linkedin.com/in/marknhenry/)

# forecasting
a
## Setting Up with AML
Container has Jupyter with Python

``` bash 
docker stop tasty_pie # stop container
docker rm tasty_pie # remove container
docker build -t "forecast-dev-env:v1" . # Build the image from Dockerfile
docker run -it -d --name tasty_pie "forecast-dev-env:v1" # Run container
docker exec -it tasty_pie /bin/bash # Log into container
```

## Setting Up with Databricks
``` bash 
docker stop brick_pie # stop container
docker rm brick_pie # remove container
docker build -t "forecast-dev-env:v2-databricks" . # Build the image from Dockerfile
docker run -it -d --name brick_pie "forecast-dev-env:v2-databricks" # Run container
docker exec -it brick_pie /bin/bash # Log into container
```

## Getting and Setting Secrets in Github
In Azure CLI run the following command, replacing your subscription id (remove the curly braces, and don't add a slash after it).  
``` bash
az ad sp create-for-rbac --name "GHCICD" --role contributor --scopes /subscriptions/{subscription_id} --sdk-auth
```

The result will be something like: 
``` json
{
  "clientId": "your_value",
  "clientSecret": "your_value",
  "subscriptionId": "your_value",
  "tenantId": "your_value",
  "activeDirectoryEndpointUrl": "your_value",
  "resourceManagerEndpointUrl": "your_value",
  "activeDirectoryGraphResourceId": "your_value",
  "sqlManagementEndpointUrl": "your_value",
  "galleryEndpointUrl": "your_value",
  "managementEndpointUrl": "your_value"
}
```

Your command will generate something like the above, but will have different values instead of **your_value** above that is between quotes.  Don't replace anything, but create the following Github Secrets: 

| Github Secret Name | Value |
|--------------------|-------------------------------------|
| AZURE_CREDENTIALS | entire output generated from `az ad sp ...` including first and last curly braces|
| AZURE_CREDENTIALS_CLIENTID | value from `clientId` from output |
| AZURE_CREDENTIALS_TENANTID | value from `tenantId` from output |
| AZURE_CREDENTIALS_CLIENTSECRET | value from `clientSecret` from output |
| AZURE_SUBSCRIPTION_ID | value from `subscriptionId` from output |

# IaC Workflows
Go to the Actions tab, run the IaC-Provision workflow.  You should have the entire environment provisioned.  