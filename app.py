from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simple demo lists (keeps state while server runs)
courses = []
users = ["Sangeetha"]
enrollments = {}

@app.route("/")
def home():
    # render index.html (no extra args required)
    return render_template("index.html")

@app.route("/courses", methods=["GET", "POST"])
def courses_page():
    if request.method == "POST":
        name = request.form.get("course_name", "").strip()
        if name and name not in courses:
            courses.append(name)
            enrollments.setdefault(name, [])
        return redirect(url_for("courses_page"))
    return render_template("courses.html", courses=courses)

@app.route("/assign", methods=["GET","POST"])
def assign_page():
    if request.method == "POST":
        course = request.form.get("course")
        user = request.form.get("user","").strip()
        if course and user:
            enrollments.setdefault(course, [])
            if user not in enrollments[course]:
                enrollments[course].append(user)
            if user not in users:
                users.append(user)
        return redirect(url_for("assign_page"))
    return render_template("assign.html", courses=courses, users=users)

@app.route("/enrolled")
def enrolled_page():
    return render_template("enrolled.html", enrollments=enrollments)

# test route to prove server is running
@app.route("/test")
def test():
    return "Server is running"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
