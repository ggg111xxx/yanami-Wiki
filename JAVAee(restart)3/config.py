#进行配置
#创建数据库对象，对数据库连接进行配置
#MYSQL所在的主机名
HOSTNAME="127.0.0.1"
#MYSQL默认监听3306
PORT=3306
USERNAME="root"
PASSWORD="gx5201314..."
#数据库名称
DATABASE="users"

DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI

#mzfisamxtxwcdhje
#邮箱配置
MAIL_SERVER="smtp.qq.com"
MAIL_USE_SSL=True
MAIL_PORT=465
MAIL_USERNAME="2421484330@qq.com"
MAIL_PASSWORD="mzfisamxtxwcdhje"
MAIL_DEFAULT_SENDER = "2421484330@qq.com"  # 添加这一行设置默认发件人