from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import inspect

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

def api(func) -> APIRouter:
    method_name = func.__name__
    path = f"/{method_name}"
    return_annotation = inspect.signature(func).return_annotation
    router = APIRouter()

    if return_annotation != inspect.Signature.empty:
        router.post(path, response_model=return_annotation)(func)
    else:
        router.post(path)(func)

    return router


if __name__ == "__main__":
    from api_calculate import calculate as m1
    app.include_router(m1)
    from api_text import text_api as m2
    app.include_router(m2)
    uvicorn.run(app, host="127.0.0.1", port=8000)
