from flask import Blueprint, render_template

user_blueprint = Blueprint('user', __name__)


# app.debug = True  # 启用调试模式，修改了代码不用重启，自动重启


@user_blueprint.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@user_blueprint.route('/ChristmasTree/', methods=["GET", "POST"])
def ChristmasTree():
    # 一棵树
    return render_template('ChristmasTree.html')


@user_blueprint.route('/PinkHeart/', methods=["GET", "POST"])
def PinkHeart():
    # 心心
    return render_template('PinkHeart.html')


@user_blueprint.route('/ChristmasGifts/', methods=["GET", "POST"])
def ChristmasGifts():
    # 很多圣诞树
    return render_template('ChristmasGifts.html')


@user_blueprint.route('/fireworks/', methods=["GET", "POST"])
def fireworks():
    # 很多圣诞树
    return render_template('fireworks.html')
