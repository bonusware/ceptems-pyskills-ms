
from flask import Blueprint, render_template, abort, request, jsonify, json

PREFIX = "/llm/api"


endpoints = Blueprint('llm', __name__)

@endpoints.route(f'{PREFIX}/query',  methods=['POST'])
def query():
    content = request.get_json(silent=True)
    q= content['query']
    
    try:
         res = ""
         
         return json.dumps({"response": str(res)})
    except Exception as err:
        print(err)
        abort(404)