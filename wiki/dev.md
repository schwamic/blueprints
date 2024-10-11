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

### Setup

1. Manage environment and dependencies via [uv](https://github.com/astral-sh/uv). Create project via `uv init <project-name>`
2. Create virtual environment via `uv venv` and activate it via `source .venv/bin/activate` ([Docs](https://fastapi.tiangolo.com/virtual-environments/#create-a-virtual-environment))

### Development

1. Run Docker `docker compose up --build --remove-orphans` for local development
2. Run tests via `TODO`

* ...
* ruff (Linter)
* FastAPI (REST) `uv add fastapi --extra standard`
* LangChain (PrompChain)
* OpenAI API to generate Missions (GPT4)

## Frontend

1. Init project via `npm create vite@latest` and choose `react` as framework

* Vite (vite)
* React
