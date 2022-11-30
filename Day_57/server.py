# Just for study



# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# def get_gender(name):
#     gender_url = f"https://api.genderize.io?name={name}"
#     gender_data = requests.get(gender_url).json()
#     gender = gender_data["gender"]
#     return gender

# def get_age(name):
#     age_url = f"https://api.agify.io?name={name}"
#     age_data = requests.get(age_url).json()
#     age = age_data["age"]
#     return age

# @app.route("/")
# def home():
#     return render_template("index.html", num = 10)

# @app.route("/guess/<name>")
# def guess(name):
#     gender = get_gender(name)
#     age = get_age(name)

#     return render_template(
#         template_name_or_list="guess.html", 
#         person_name=name.title(), 
#         gender=gender,
#         age=age
#     )



# if __name__ == "__main__":
#     app.run(debug=True)