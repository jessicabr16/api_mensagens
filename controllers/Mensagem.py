from flask import Flask, render_template, request, redirect, flash, url_for
from models.Mensagem import Mensagem
from utils import db

from flask import Blueprint

bp_mensagens = Blueprint("mensagens", __name__, template_folder='templates')

@bp_mensagens.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('create.html')
    elif request.method=='POST':
        mensagem=Mensagem(request.form['conteudo'])
        db.session.add(mensagem)
        db.session.commit()
        return redirect(url_for('.recovery'))

@bp_mensagens.route('/recovery', defaults={'id': 0})
@bp_mensagens.route('/recovery/<int:id>')
def recovery(id):
    if (id==0):
        mensagens = Mensagem.query.all()
        return render_template('recovery.html', mensagens=mensagens)
    else:
        mensagem = Mensagem.query.get(id)
        return render_template('charme.html', mensagem=mensagem)

@bp_mensagens.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if id and request.method=='GET':
        mensagem=Mensagem.query.get(id)
        return render_template('update.html', mensagem=mensagem)
    if request.method=='POST':
        mensagem = Mensagem.query.get(id)
        mensagem.conteudo=request.form['conteudo']
        db.session.add(mensagem)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect(url_for('.recovery', id=id))

@bp_mensagens.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        mensagem=Mensagem.query.get(id)
        return render_template('delete.html', mensagem = mensagem)
    if request.method=='POST':
        mensagem=Mensagem.query.get(id)
        db.session.delete(mensagem)
        db.session.commit()
        return redirect(url_for('.recovery'))