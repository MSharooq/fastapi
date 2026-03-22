from fastapi import FastAPI, HTTPException, File, UploadFile, Form , Depends
from app.schemas import PostCreate
from app.db import *
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI()):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan = lifespan)


@app.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        caption: str = Form(""),
        session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption = caption,
        url = "dummy url",
        file_type = "photo",
        flie_name= "dummy name"
    )

    session.add(post)
    await session.commit()