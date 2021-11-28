from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import PostRequestSchema, PostResponseSchema
from db.database import get_db
from db import db_post
from typing import List

router = APIRouter(
    prefix='/api/v1/posts',
    tags=['posts']
)


@router.post('', response_model=PostResponseSchema)
def create(request: PostRequestSchema, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get('/all', response_model=List[PostResponseSchema])
def get_all_post(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.get('/{title}}', response_model=PostResponseSchema)
def get_post_by_title(title: str, db: Session = Depends(get_db)):
    return db_post.get_post_by_title(title, db)


@router.get("/{author}", response_model=List[PostResponseSchema])
def get_post_by_author(author: str, db: Session = Depends(get_db)):
    return db_post.get_post_by_author(author, db)

