from flask_script import Manager
from Demo_utils.app import create_app
from Demo_utils.logger import Log as log

app = create_app()
manage = Manager(app)

if __name__ == '__main__':
    try:
        manage.run()
    except Exception as e:
        log.error("启动异常", e)
