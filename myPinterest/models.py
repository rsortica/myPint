# created the database structure
from myPinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    __tablename__ = 'usuario'  # Specify the table name
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Post", backref="usuario", lazy=True)

class Post(database.Model):
    __tablename__ = 'posts'  # Specify the table name
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    create_data = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)  # Changed to use callable
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)  # Fixed typo: 'ForeignKey'


