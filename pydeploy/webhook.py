from threading import Thread
from bottle import Bottle, request, response
from pydeploy.command_chain import CommandChain
import pydeploy.config as config

app = Bottle()

running_threads = []


@app.post("/" + config.route)
def deploy():
    chain = CommandChain.load_from_config("")
    for cmd in chain.commands:
        cmd.kill()

    data = request.json
    ref = data['ref']
    pusher_name, pusher_email = data['pusher']['name'], data['pusher']['email']

    print("Push Received : ")
    print("Ref : {}".format(ref))
    response.content_type = 'text/text; charset=UTF8'

    chain = CommandChain.load_from_config("")
    t = Thread(target=chain.execute)
    t.start()
    running_threads.append(t)

    return u"{} {} {}".format(ref, pusher_name, pusher_email)