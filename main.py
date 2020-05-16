from flask import Flask, request
from flask import Response
from gitif import Git
from config import Config

repos = Config.repos

app = Flask(__name__)

@app.route('/pull/<string:repo>', methods=['GET', 'POST'])
def pullrepo(repo):
    if not repo in repos:
        return Response(status=404)
    git = Git(repo)
    branch = request.args.get('branch')
        return Response(status=403)
    Git(repo).pull(branch)
    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
