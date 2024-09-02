import wtforms
from flask import Blueprint, render_template, request, jsonify
import string
import random
from models import Determine_Email_Model, UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Message
from exts import mail, db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.json
        id = data['id']
        password = data['password']

        user = UserModel.query.filter_by(id=id).first()
        if user and check_password_hash(user.password, password):
            return jsonify({"message": f"欢迎回来！{user.username}"})

        return jsonify({"message": "用户名或密码错误"}), 400

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.json
        email = data['email']
        verification_code = data['verificationCode']
        username = data['username']
        password = data['password']
        confirm_password = data['confirmPassword']

        code_record = Determine_Email_Model.query.filter_by(email=email).order_by(Determine_Email_Model.id.desc()).first()
        if code_record.determine != verification_code:
            return jsonify({"message": "验证码错误"}), 400

        if password != confirm_password:
            return jsonify({"message": "密码不一致"}), 400

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        new_user = UserModel(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": f"注册成功，您的Yanami账号是：{new_user.id},请妥善保管"})

    return render_template("register.html")

@bp.route("/determine/email", methods=['GET'])
def get_email():
    email = request.args.get("email")
    determine = "".join(random.sample(string.digits, 4))
    message = Message(subject="Yanami注册验证码",
                      recipients=[email],
                      body=f"您的验证码是:{determine},请勿泄露给他人")
    mail.send(message)

    email_determine = Determine_Email_Model(email=email, determine=determine)
    db.session.add(email_determine)
    db.session.commit()

    return "验证码已发送"
