# Developer Documentation

## DevOps

Install and setup the following technologies:

### [Docker Desktop](https://docs.docker.com/desktop/) (Container + Kubernetes)

1. Activate Kubernetes via settings
2. Setup context for Kubernetes ([Docs](https://docs.docker.com/desktop/kubernetes/)):
```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
```

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

* Code Style: https://peps.python.org/pep-0008/#naming-conventions

### Setup

1. Manage environment and dependencies via [uv](https://github.com/astral-sh/uv). Create project via `uv init <project-name>`
2. Create virtual environment via `uv venv` and activate it via `source .venv/bin/activate` ([Docs](https://fastapi.tiangolo.com/virtual-environments/#create-a-virtual-environment))
3. Setup [Docker for FastAPI](https://fastapi.tiangolo.com/deployment/docker/?h=docker#fastapi-in-containers-docker) + [FullStack-Template](https://github.com/fastapi/full-stack-fastapi-template/tree/master)

### Development Environment

- [VS Code Workspaces](https://code.visualstudio.com/docs/editor/workspaces)
- [VS Code Dev Containers](https://www.youtube.com/watch?v=dihfA7Ol6Mw)

#### Local Terminal

1. Run Docker `docker compose up --build --remove-orphans` to start server

#### Dev Container

1. VSCode: Reopen `/backend` in container. (Only once: +Connect to blueprints repository, +Install extension in vs-code)
2. Run `source .venv/bin/activate` (test via `which python`)
3. Run `uv sync`
4. Run tests via `uv tool run pytest` or just `pytest` ([Docs](https://docs.pytest.org/en/stable/how-to/usage.html))
5. Run linter via `ruff check app/` ([Docs](https://docs.astral.sh/ruff/linter/))
6. Run tests via `pytest -s -k 'regex'`

#### Misc

- FastAPI (REST) `uv add fastapi --extra standard`
- LangChain (PrompChain)
- OpenAI API to generate Missions (GPT4)

## Frontend

1. Init project via `npm create vite@latest` and choose `react` as framework

- Vite (vite)
- React
