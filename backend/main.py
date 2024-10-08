from fastapi import FastAPI

from .core import db
from .routers import (pdf_files, accounts)

db.Base.metadata.create_all(bind=db.engine)
app = FastAPI(title='iHate PyPDF')
app.include_router(pdf_files.router)
app.include_router(accounts.router)
