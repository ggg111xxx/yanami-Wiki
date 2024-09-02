#与用户相关的内容（登陆注册）
from flask import Blueprint

bp=Blueprint("user",__name__,url_prefix="/")#首页，进去就是

# http://127.0.0.1:5000
@bp.route("/")
def index():
    pass