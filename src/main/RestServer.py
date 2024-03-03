import sys

from flask import Flask
from rest.Blueprints import endpoints

f
from rest.config.Constants import swagger, config, template

from flasgger import Swagger


"""
Author          : Amr Salem
Create Date     : 18-02-2024
File            : RestServer.py
"""

app = Flask(__name__)

def restServer():

  app.config['SWAGGER'] = swagger
  

  #swagger_project = Swagger(app, config=config, template=template)
  #swagger_project.register_blueprint(apppack_endpoints)

 
  #app.register_blueprint(generated_code_endpoints)


  Swagger(app, template=template, )

  return app


@app.route('/check-alive')
def hello():
    return 'Um alive!'


if __name__ == '__main__':  
  try:
    port = int(sys.argv[1])
  except Exception:
    port = 8081

  restServer().run(host='0.0.0.0', port=port, debug=True, use_reloader=True)