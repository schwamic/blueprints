# Backend

This project was bootstrap via `uv` and uses the framework `fastapi`.

## Modular (3-)Layered Architecutre

```
- Common
|- Clients
|- Middlewares
|- BackgroundTasks
|- (...)
- Module
|- Controller
|- Service
|- Entity
|- (Dto, ...)
```

- [Sample NestJS app](https://github.com/nestjs/nest/tree/master/sample/01-cats-app)
- [FastAPI: Bigger Apps](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## Wiki

- [Development](../wiki/dev.md)
