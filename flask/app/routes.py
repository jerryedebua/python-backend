from app import App

@App.route('/')
@App.route('/index')
@App.route('/api')
@App.route('/api/index')
def index():
  key = 'state'
  return { key: 'Okay' }


@App.route('/user')
@App.route('/api/user')
def user():
  return {
    'id': 1, 'name': 'Harvey'
  }
