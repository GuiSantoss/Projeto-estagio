from sqlalchemy.orm import Session
import models, schemas

def get_empresas(db: Session):
    return db.query(models.Empresa).all()

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_obrigacoes(db: Session):
    return db.query(models.ObrigacaoAcessoria).all()

def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao
