from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel
import uuid

app = FastAPI()

# Criação do Crud referente aos produtos.

class Produto(BaseModel):
    uuid: str
    nome : str
    preco : float
    qtd : int 

class RequestProduto(BaseModel):
    nome : str
    preco : float
    qtd : int 

produtos = [] 

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def cadastra_produto(payload: RequestProduto):

    try: 
        produto = Produto(uuid= str(uuid.uuid1()) , nome=payload.nome, preco= payload.preco, qtd = payload.qtd)

    except:
         raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST)
    
    produtos.append(produto)

@app.get('/produtos', status_code=status.HTTP_200_OK)
def lista_produtos():

    return produtos

@app.get('/produtos/{id}', status_code= status.HTTP_200_OK)
def lista_produto(id: str):
    resultado = list(filter(lambda p: p.uuid == id , produtos))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Produto de uuid = '{}' não foi encontrado.".format(id))

    return resultado

@app.put('/produtos/{id}')
def alterar_produto(id: str, payload: RequestProduto):
    resultado = list(filter(lambda p: p.uuid == id , produtos))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Produto de uuid = '{}' não foi encontrado.".format(id))

    resultado[0].nome = payload.nome
    resultado[0].preco = payload.preco
    resultado[0].qtd = payload.qtd

    return resultado[0]

@app.delete("/produtos/{id}")
def deletar_produtos(id: str):
    resultado = list(filter(lambda p: p.uuid == id , produtos))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Produto de uuid = '{}' não foi encontrado.".format(id))

    return produtos.remove(resultado[0])

#Criação do crud de Categorias

class Categoria(BaseModel):
    uuid : str
    nome : str

class RequestCategoria(BaseModel):
    nome: str

categorias = []

@app.post('/categoria', status_code=status.HTTP_201_CREATED)
def cadastra_categoria(payload: RequestCategoria):

    try: 
        categoria = Categoria(uuid= str(uuid.uuid1()) , nome=str(payload.nome))

    except:
         raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST)
    
    categorias.append(categoria)

@app.get('/categorias', status_code=status.HTTP_200_OK)
def lista_categorias():
    return categorias

@app.get('/categorias/{id}', status_code= status.HTTP_200_OK)
def lista_produto(id: str):
    resultado = list(filter(lambda c: c.uuid == id , categorias))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Categoria de uuid = '{}' não foi encontrada.".format(id))

    return resultado

@app.put('/categorias/{id}')
def alterar_categoria(id: str, payload: RequestCategoria):
    resultado = list(filter(lambda c: c.uuid == id , categorias))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Categoria de uuid = '{}' não foi encontrado.".format(id))

    resultado[0].nome = payload.nome

    return resultado[0]

@app.delete("/categorias/{id}")
def deletar_categorias(id: str):
    resultado = list(filter(lambda c: c.uuid == id , categorias))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Produto de uuid = '{}' não foi encontrado.".format(id))

    categorias.remove(resultado[0])

#Crud de Fornecedores

class Fornecedor(BaseModel):
    uuid : str
    nome : str
    cnpj : str

class RequestFornecedor(BaseModel):
    nome: str
    cnpj: str


fornecedores = []

@app.post('/fornecedor', status_code=status.HTTP_201_CREATED)
def cadastra_fornecedor(payload: RequestFornecedor):

    try: 
        fornecedor = Fornecedor(uuid= str(uuid.uuid1()) , nome=str(payload.nome), cnpj=str(payload.cnpj))

    except:
         raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST)
    
    fornecedores.append(fornecedor)

@app.get('/fornecedores', status_code=status.HTTP_200_OK)
def lista_fornecedores():

    return fornecedores

@app.get('/fornecedores/{id}', status_code= status.HTTP_200_OK)
def lista_fornecedor(id: str):
    resultado = list(filter(lambda f: f.uuid == id , fornecedores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Fornecedor de uuid = '{}' não foi encontrada.".format(id))

    return resultado

@app.put('/fornecedores/{id}')
def alterar_fornecedor(id: str, payload: RequestFornecedor):
    resultado = list(filter(lambda f: f.uuid == id , fornecedores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Fornecedor de uuid = '{}' não foi encontrado.".format(id))

    resultado[0].nome = payload.nome
    resultado[0].cnpj = payload.cnpj

    return resultado[0]

@app.delete("/fornecedores/{id}")
def deletar_fornecedor(id: str):
    resultado = list(filter(lambda f: f.uuid == id , fornecedores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Fornecedor de uuid = '{}' não foi encontrado.".format(id))

    categorias.remove(resultado[0])


#Crud de Compradores

class Comprador(BaseModel):
    uuid: str
    nome: str
    cpf : str
    end : str

class RequestComprador(BaseModel):
    nome: str
    cpf : str
    end : str

compradores = []

@app.post('/comprador', status_code=status.HTTP_201_CREATED)
def cadastra_comprador(payload: RequestComprador):

    try: 
        comprador = Comprador(uuid= str(uuid.uuid1()) , nome=str(payload.nome), cnpj=str(payload.cpf), end =str(payload.end))

    except:
         raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST)
    
    compradores.append(comprador)

@app.get('/compradores', status_code=status.HTTP_200_OK)
def lista_compradores():

    return compradores

@app.get('/compradores/{id}', status_code= status.HTTP_200_OK)
def lista_comprador(id: str):
    resultado = list(filter(lambda c: c.uuid == id , compradores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comprador de uuid = '{}' não foi encontrada.".format(id))

    return resultado

@app.put('/compradores/{id}')
def alterar_comprador(id: str, payload: RequestComprador):
    resultado = list(filter(lambda c: c.uuid == id , compradores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comprador de uuid = '{}' não foi encontrado.".format(id))

    resultado[0].nome = payload.nome
    resultado[0].cpf = payload.cpf
    resultado[0].end = payload.end

    return resultado[0]


@app.delete("/compradores/{id}")
def deletar_comprador(id: str):
    resultado = list(filter(lambda c: c.uuid == id , compradores))

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comprador de uuid = '{}' não foi encontrado.".format(id))

    categorias.remove(resultado[0])
























