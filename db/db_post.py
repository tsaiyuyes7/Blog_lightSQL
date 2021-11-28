# from router.schemas import PostRequestSchema
# from sqlalchemy.orm.session import Session
# from db.models import DbBlog
#
#
# def create(db: Session, request: PostRequestSchema):
#     new_post = DbBlog(
#         title=request.title,
#         author=request.author,
#         content=request.content
#     )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post
#
#
# def get_all(db: Session):
#     return db.query(DbBlog).all()
#
#
# def get_post_by_author(author: str, db: Session):
#     return db.query(DbBlog).filter(DbBlog.author == author).all()
#
#
# def get_post_by_title(title: str, db: Session):
#     return db.query(DbBlog).filter(DbBlog.title == title).all()

from router.schemas import PostRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbPost


def create(db: Session, request: PostRequestSchema):
    new_product = DbPost(
        title=request.title,
        author=request.author,
        content=request.content
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session):
    return db.query(DbPost).all()


def get_post_by_title(title: str, db: Session):
    return db.query(DbPost).filter(DbPost.title == title).first()


def get_post_by_author(
        author: str,
        db: Session):
    return db.query(DbPost).filter(DbPost.author == author).all()