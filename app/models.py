from app import db
from flask import abort


class Video(db.Model):
    """
    视频 Model
    """
    __tablename__ = 'videos'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 视频id
    vid = db.Column(db.String(50))
    # 封面图片
    coverUrl = db.Column(db.Text)
    # 详情描述
    desc = db.Column(db.Text)
    # 概要
    synopsis = db.Column(db.Text)
    # 标题
    title = db.Column(db.String(100))
    # 发布时间
    updateTime = db.Column(db.Integer)
    # 主题
    theme = db.Column(db.String(10))
    # 是否已删除？（逻辑）
    isDelete = db.Column(db.Boolean, default=False)

    def to_json(self):
        """
        完成Video数据模型到JSON格式化的序列化字典转换
        """
        json_blog = {
            'id': self.vid,
            'coverUrl': self.coverUrl,
            'desc': self.desc,
            'synopsis': self.synopsis,
            'title': self.title,
            'updateTime': self.updateTime
        }
        return json_blog


def getHomepageData():

    result = {}
    # 获取banner
    banners = Video.query.filter_by(theme='banner')
    result['banner'] = [banner.to_json() for banner in banners]
    # 获取homepage
    first = Video.query.filter_by(theme='hot').all()
    print('----first---',type(first))
    second = Video.query.filter_by(theme='dramatic').all()
    third = Video.query.filter_by(theme='idol').all()
    if len(first) and len(second) and len(third):
        homepage = [{'Hot Broadcast': [item.to_json() for item in first]},
                    {'Dramatic Theater': [item.to_json() for item in second]},
                    {'Idol Theatre': [item.to_json() for item in third]}]
        result['homepage'] = homepage
        return result
    else:
        abort(404)


class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"  # 表名

    # 字段名        类型         约束
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    # 1方定义关系  反向引用
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观 而不是显示内存地址"""
        return "Role object: name=%s" % self.name


class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    # 多方定义外键 指向1方主键
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User object: name=%s" % self.name


class User3(db.Model):
    """用户表"""
    __tablename__ = "tbl_users5"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return "User object: name=%s" % self.name