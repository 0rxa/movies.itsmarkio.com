from flask import Flask, request
from flask import Response
from gitif import Git

app = Flask(__name__)

repos = [ 'web', 'relay' ]

@app.route('/pull/<string:repo>', methods=['GET', 'POST'])
def pullrepo(repo):
    if not repo in repos:
        return Response(status=404)
    branch = request.args.get('branch')
    Git(repo).pull(branch)
    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
