from fastapi import APIRouter
from fastapi import Request, Response

from settings import templates
router = APIRouter(
    tags= ['maps',]
)


@router.get("/list_maps/")
async def get_list(request: Request) -> Response :
    return Response("Ok", status_code=200)

@router.get("/map/{id}")
async def get_maps(request: Request) -> Response :
    return Response("Ok", status_code=200)

@router.post("/map/{id}")
async def get_maps(request: Request) -> Response :
    return Response("Ok", status_code=200)

