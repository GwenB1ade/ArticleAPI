from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


async def exception_500(request: Request, exc):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


async def exception_http(request: Request, ext: HTTPException):
    return JSONResponse(status_code=ext.status_code, content={"detail": ext.detail})


article_not_found = HTTPException(status_code=404, detail="Article not found")
