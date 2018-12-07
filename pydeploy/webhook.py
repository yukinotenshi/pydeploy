from bottle import Bottle, request, response
import pydeploy.config as config

app = Bottle()


@app.post("/" + config.route)
def deploy():
    data = request.json
    ref = data['ref']
    pusher_name, pusher_email = data['pusher']['name'], data['pusher']['email']

    print("Push Received : ")
    print("Ref : {}".format(ref))
    response.content_type = 'text/text; charset=UTF8'

    return u"{} {} {}".format(ref, pusher_name, pusher_email)
