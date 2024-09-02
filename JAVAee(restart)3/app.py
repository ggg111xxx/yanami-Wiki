from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
import config

# 连接并调用各文件
from exts import db, mail
from blueprints.user import bp as userbp
from blueprints.auth import bp as authbp

app = Flask(__name__)  # 创建一个Flask应用实例
app.config.from_object(config)  # 读取绑定配置信息

db.init_app(app)  # 绑定 SQLAlchemy 实例
mail.init_app(app)  # 绑定 Flask-Mail 实例

CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有来源的请求

migrate = Migrate(app, db)

app.register_blueprint(userbp)
app.register_blueprint(authbp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)

