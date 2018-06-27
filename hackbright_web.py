"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


# @app.rounte("/")
# def index():
#     pass


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    # github = 'jhacks'

    first, last, github = hackbright.get_student_by_github(github)

    project_lst = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_lst=project_lst)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/show_form")
def show_form():
    return render_template("create_new_student.html")


@app.route("/create_new_student", methods=['POST'])
def create_new_student():

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("confirmation.html",
                           first_name=first_name,
                           last_name=last_name,
                           github=github)


@app.route("/project")
def show_project_listing():

    title = request.args.get('title')

    project_lst_max_grade = hackbright.get_project_by_title(title)

    return render_template("project.html", project_lst_max_grade=project_lst_max_grade)

@app.route("/display_confirmation")
def show_confirmation():

    return 




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
