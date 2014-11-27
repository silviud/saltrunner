from salt import client
from flask import Flask, request, current_app


app = Flask(__name__)

@app.route('/chef_client', methods=['POST'])
def run_chef():
    """ executes chef client - requires Chef server
    on all minions
    :returns jobId:
    """
    cmd = app.request.POST.get('cmd')
    salt_client = client.LocalClient()
    return 99


if __name__ == '__main__':
    app.run(debug=True)
