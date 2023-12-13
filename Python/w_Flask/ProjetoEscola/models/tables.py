from ProjetoEscola import db

class Students_Inf(db.Model):
    __tablename__ = "Students_List"

    id = db.Collumn(db.Integer, primary_key=True)
    name = db.model(db.String, nullable=False)
    age = db.model(db.Integer, nullable=False)
    cpf = db.model(db.String, unique=True)
    email = db.Collumn(db.String, unique=True)

    def __init__(self, name, age, cpf, email):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email

    def __repr__(self):
        return "<Aluno: {self.name}\nMatricula: {self.id}>"