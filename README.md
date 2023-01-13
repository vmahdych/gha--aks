# Task: Create GitHub Actions workflow

## Requirements:
- [ ] Job 1 - Setup environment: Container Registry and Azure Kubernetes Service
- [ ] Job 2 - Build / Push to ACR: build image, scan image, and push image to ACR
- [ ] Job 3 - Deploy to AKS
- [ ] Make sure Docker file is [secure](https://dev.to/tomoyamachi/how-to-keep-secure-your-docker-image-2hj2) enough


### Useful resources:



### Azure CLI commands that have been used during environment setup:

- Login:
  ```bash
  az login
  ```
- Create resourceGroup:
  ```bash
  az group create --name <RG_NAME> --location <SUITABLE_LOCATION>
  ```
- Create ACR:
  ```bash
  az acr create --resource-group <RG_NAME> -n <ACR_NAME> --sku Basic
  ```
-  Create a service principal for GitHub Actions workflow:
  ```bash
  az ad sp create-for-rbac --name <SERVICE_PRINCIPAL_NAME> --role "contributor" --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP_NAME> --sdk-auth
  ```
- Grant GitHub Actions service principal with the permissions to both pull and push images to Azure Container Registry:
  - Get the id of our Azure Container Registry
  ```bash
  registryId=$(az acr show --name <registry-name> --query id --output tsv)
  ```
  - Grant the 'AcrPush' role to our service principal
  ```bash
  az role assignment create --assignee <ClientId> --scope $registryId --role AcrPush
  ```
  - Grant the 'AcrPull' role to our service principal
  ```bash
  az role assignment create --assignee <ClientId> --scope $registryId --role AcrPull
  ```


