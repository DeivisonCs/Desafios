from flask import Blueprint, render_template, request
from database import db
from models.tables import Students_Inf

bp_Students = Blueprint("Students", __name__, template_folder="templates")

@bp_Students.route('/create', methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template("add_student.html")

    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")
        cpf = request.form.get("cpf")
        email = request.form.get("email")

        User = Students_Inf(name, age, cpf, email) 
        db.session.add(User)
        db.session.commit()
        return "Dados Cadastrados"


@bp_Students.route('/list')
def list_students():
    Students_all = Students_Inf.query.all()
    return render_template("list_students.html", Students_all=Students_all)