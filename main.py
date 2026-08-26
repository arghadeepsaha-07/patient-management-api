from fastapi import FastAPI,HTTPException,status
from Database.database_engine import engine
from Database.database_models import Base
from Get_Router.get_router import router as router_get
from Delete_Router.delete_router import router as router_delete
from Post_Router.post_router import router as router_create
from Put_router.put_router import router as router_update

app = FastAPI(title="Patient Management System",description="This is a patient management system where we manage patients details !")

Base.metadata.create_all(bind=engine)


app.include_router(router_get)
app.include_router(router_create)
app.include_router(router_update)
app.include_router(router_delete)
# app.include_router("post_router.py")
# app.include_router("put_router.py")
# app.include_router("delete_router.py")
