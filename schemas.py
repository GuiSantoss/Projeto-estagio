from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int

    class Config:
        orm_mode = True

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        orm_mode = True
