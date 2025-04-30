from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Mensagem(BaseModel):
    id: int
    conteudo: str

class MensagemCreate(BaseModel):
    conteudo: str

mensagens: List[Mensagem] = []

@app.post("/mensagens", response_model=Mensagem)
def criar_mensagem(mensagem: MensagemCreate):
    nova_id = len(mensagens) + 1
    nova_mensagem = Mensagem(id=nova_id, conteudo=mensagem.conteudo)
    mensagens.append(nova_mensagem)
    return nova_mensagem

@app.get("/mensagens", response_model=List[Mensagem])
def listar_mensagens():
    return mensagens

@app.get("/mensagens/{id}", response_model=Mensagem)
def obter_mensagem(id: int):
    for msg in mensagens:
        if msg.id == id:
            return msg
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")

@app.put("/mensagens/{id}", response_model=Mensagem)
def atualizar_mensagem(id: int, nova: MensagemCreate):
    for msg in mensagens:
        if msg.id == id:
            msg.conteudo = nova.conteudo
            return msg
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")

@app.delete("/mensagens/{id}")
def deletar_mensagem(id: int):
    for i, msg in enumerate(mensagens):
        if msg.id == id:
            mensagens.pop(i)
            return {"mensagem": "Deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")
