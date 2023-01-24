from fastapi import APIRouter
from fastapi import Request, Response

from settings import templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    tags=['auth',]
)


@router.get("/login/", response_class=HTMLResponse)
async def get_login(request: Request) -> Response:
    return templates.TemplateResponse("item.html", {"request": request})


@router.post("/login/")
async def get_login(request: Request) -> Response :
    return Response("Ok", status_code=200)
