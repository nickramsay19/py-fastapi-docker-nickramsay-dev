from __future__ import annotations
from typing import Any, Optional, Callable
from peewee import SqliteDatabase, Model, CharField, IntegerField
import os

# setup database file
APP_ROOT: str = os.path.dirname(os.path.abspath(__file__))
#db = SqliteDatabase(f"{APP_ROOT}/db/posts.db", pragmas={'journal_mode': 'wal'})
db = SqliteDatabase(f"./db/posts.db", pragmas={'journal_mode': 'wal'})

POST_MAX_TITLE_LEN = 100
POST_MAX_BODY_LEN = 100_000 

class BaseModel(Model):
    class Meta:
        database = db

class Post (BaseModel):
    id = IntegerField(unique=True, null=False, index=True, primary_key=True)
    title = CharField(max_length=POST_MAX_TITLE_LEN, null=False)
    body = CharField(max_length=POST_MAX_BODY_LEN, null=False)
