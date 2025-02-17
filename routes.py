from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/empresas", response_model=list[schemas.EmpresaResponse])
def listar_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db)

@router.post("/empresas", response_model=schemas.EmpresaResponse)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db, empresa)

@router.get("/obrigacoes", response_model=list[schemas.ObrigacaoAcessoriaResponse])
def listar_obrigacoes(db: Session = Depends(get_db)):
    return crud.get_obrigacoes(db)

@router.post("/obrigacoes", response_model=schemas.ObrigacaoAcessoriaResponse)
def criar_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao(db, obrigacao)
