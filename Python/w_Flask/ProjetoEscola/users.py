from flask import Blueprint, render_template, request

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

        return "Dados Recebidos"