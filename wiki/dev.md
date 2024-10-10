# Developer Documentation

## DevOps

Install and setup the following technologies:

### [Docker Desktop](https://docs.docker.com/desktop/) (Container, Kubernetes)

1. Activate Kubernetes via settings
2. Setup context for Kubernetes ([Docs](https://docs.docker.com/desktop/kubernetes/)):
```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
```

2. Setup [Docker for FastAPI](https://fastapi.tiangolo.com/deployment/docker/?h=docker#fastapi-in-containers-docker)

### [mogenius](https://mogenius.com) (Kubernetes Management)

1. Create an organisation
2. Create a cluster -> Install mogenius operator via helm ([Docs](https://docs.mogenius.com/tutorials/how-to-deploy-docker-container-on-kubernetes))
```bash
# find old deployment
helm list --all-namespaces
# delete old deployment
helm uninstall <deployment name> --namespace <namespace_name>
# install new deployment
helm install [...]
```

## Backend

1. Create a virtual environment ([Docs](https://fastapi.tiangolo.com/virtual-environments/#create-a-virtual-environment))
2. Install FastAPI and save it via `uv pip freeze > requirements.txt`

* FastAPI (REST)
* LangChain (PrompChain)
* OpenAI API to generate Missions (GPT4)

## Frontend

* React
