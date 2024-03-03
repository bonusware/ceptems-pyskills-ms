template = {
    "swagger": "2.0",
    "info": {
      "title": "Ceptems App Pack API",
      "description": "AI Integrations with Ceptems App Pack API",
      "version": "1.0"
    }
  }

swagger = {
    'title': 'Ceptems App Pack API',
    'uiversion': 2,
    'template': './resources/flasgger/swagger_ui.html'
  }
  
config={'specs': [
    {
        'endpoint': 'apispec_1',
        'route': '/apispec_1.json',
        'rule_filter': lambda rule: True,  # all in
        'model_filter': lambda tag: True,  # all in
    }
]}