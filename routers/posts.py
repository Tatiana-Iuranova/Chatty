from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from models import User, Post
from schemas import PostCreate, PostResponse
from utils.security import get_current_user
from database import get_db
from typing import List

router = APIRouter()


@router.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(title=post.title, content=post.content, user_id=current_user.id)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


@router.get("/posts", response_model=List[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post))
    posts = result.scalars().all()
    return posts


@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post_update: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    post.title = post_update.title
    post.content = post_update.content
    await db.commit()
    await db.refresh(post)
    return post


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    await db.delete(post)
    await db.commit()
    return {"message": "Post deleted"}from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from models import User, Post
from schemas import PostCreate, PostResponse
from utils.security import get_current_user
from database import get_db
from typing import List

router = APIRouter()


@router.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(title=post.title, content=post.content, user_id=current_user.id)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


@router.get("/posts", response_model=List[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post))
    posts = result.scalars().all()
    return posts


@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post_update: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    post.title = post_update.title
    post.content = post_update.content
    await db.commit()
    await db.refresh(post)
    return post


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    await db.delete(post)
    await db.commit()
    return {"message": "Post deleted"}