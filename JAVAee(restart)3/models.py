from exts import db
from datetime import datetime
class UserModel(db.Model):
    __tablename__ = "users"  # 类映射到数据库中的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    jointime=db.Column(db.DateTime,default=datetime.now)

class Determine_Email_Model(db.Model):
    __tablename__ = "Determine_Email"  # 类映射到数据库中的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    determine = db.Column(db.String(50), nullable=False)