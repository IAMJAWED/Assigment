"""Module web Doctsring."""
import web
import json

URLS = (
    '/v1/diff/left', 'Left'
    )

APP = web.application(URLS, globals())
RENDER = web.template.render('templates/', base="layout")
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
# This is a list.
print(type(best_food_chains))
# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
# We've successfully converted our list to a string.
print(type(best_food_chains_string))
# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

class Left(object):
    """Class Doctsring."""
   # def GET(self):
      #  """Method GET Doctsring."""
       # return RENDER.hello_form()

    #def POST(self):
      #  """Method POST Doctsring."""
       # form = web.input(name="Nobody", greet="Hello")
       # greeting = "%s, %s" % (json.dumps(best_food_chains), json.loads(best_food_chains_string))
      #  return  "Hello"#RENDER.index(greeting=greeting)

    def api_message():
        if request.headers['Content-Type'] == 'text/plain':
            return "Text Message: " + request.data

        elif request.headers['Content-Type'] == 'application/json':
            return "JSON Message: " + json.dumps(request.json)

        elif request.headers['Content-Type'] == 'application/octet-stream':
            f = open('./binary', 'wb')
            f.write(request.data)
            f.close()
            return "Binary message written!"

        else:
            return "415 Unsupported Media Type ;)"
    
if __name__ == "__main__":
    APP.run()
