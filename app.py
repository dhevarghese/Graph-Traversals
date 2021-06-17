from flask import Flask, render_template, send_file, request, redirect, url_for, g, session
import matplotlib as plt
plt.use('Agg')
from io import BytesIO
import networkx as nx
import sys
from random import randrange 
from graph import Graph
from vertex import Vertex
from flask_session import Session


app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

nodes=0
@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        session["graph"]=Graph()
        session["nodes"]=1
        return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    #return render_template('menupage.html')
    if request.method=='POST':
        nodes = request.form.get('number-of-new-nodes')
        print("nodes :" + str(nodes))
        return render_template("menupage.html", nodes=nodes)
    else:
        nodes = request.form.get('number-of-new-nodes')
        print(nodes, file=sys.stderr)
        return render_template('menupage.html', graph=session["graph"])


@app.route('/random', methods=['GET', 'POST'])
def random():
    session["graph"].clearVertices()
    session["nodes"] = 1
    startNode = 0
    endNode = 0
    storeEdges = {}
    nodes = randrange(3,12,1)
    print(nodes)
    startNode = session["nodes"]
    endNode = session["nodes"]+ int(nodes)
    session["nodes"] += int(nodes)
    for ct in range(startNode, endNode): 
        session["graph"].add_vertex(Vertex(ct))
    nodeRange = {"start":startNode, "end":endNode}
    edges = randrange(1, (nodes*(nodes-1))/2, 1)
    i = 0
    while(i < edges):
        nodeSt = randrange(nodeRange["start"],nodeRange["end"],1)
        nodeEnd = randrange(nodeRange["start"],nodeRange["end"],1)
        if nodeSt != nodeEnd and {"st": nodeSt, "end": nodeEnd} not in storeEdges.values():
            session["graph"].add_edge(nodeSt,nodeEnd)
            storeEdges[i] = {"st": nodeSt, "end": nodeEnd}
            i += 1
    return {"one": nodeRange, "two": storeEdges}
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    startNode = 0
    endNode = 0
    if request.method=='POST':
        nodes = request.form.get('nodes')
        print("From add:" + str(nodes))
        startNode = session["nodes"]
        endNode = session["nodes"]+ int(nodes)
        session["nodes"] += int(nodes)
        for ct in range(startNode, endNode): 
            session["graph"].add_vertex(Vertex(ct))
    nodeRange = {"start":startNode, "end":endNode}
    return nodeRange

@app.route('/delete', methods=['POST'])
def delete():
    nodeDel = int(request.form.get('node'))
    return str((session["graph"].delete_vertex(Vertex(nodeDel))).key)
    
@app.route('/addEdge', methods=['POST'])
def addEdge():
    nodeSt = int(request.form.get('st'))
    nodeEnd = int(request.form.get('end'))
    session["graph"].add_edge(nodeSt,nodeEnd)
    return {"st": nodeSt, "end": nodeEnd}

@app.route('/deleteEdge', methods=['POST'])
def deleteEdge():
    nodeSt = int(request.form.get('st'))
    nodeEnd = int(request.form.get('end'))
    retVal = session["graph"].delete_edge(nodeSt,nodeEnd)
    print(retVal)
    if retVal == None:
        return {"pos": False}
    else:
        return {"pos": True, "st": nodeSt, "end": nodeEnd}

@app.route('/DFS', methods=['POST'])
def dfs():
    print(request.form.get('st'))
    nodeSt = int(request.form.get('st'))
    retVal = session["graph"].DFSF(nodeSt)
    print(retVal)
    if retVal == None:  
        return {"pos": False}
    else:
        return {"pos": True, "order": retVal}

@app.route('/BFS', methods=['POST'])
def bfs():
    print(request.form.get('st'))
    nodeSt = int(request.form.get('st'))
    retVal = session["graph"].BFSF(nodeSt)
    print(retVal)
    if retVal == None:
        return {"pos": False}
    else:
        return {"pos": True, "order": retVal}

@app.route('/Adjmat', methods=['POST'])
def adjm():
    retVal=[]
    retVal = session["graph"].adjmat()
    print(retVal)
    for i in range(0,session["graph"].size):
        for j in range(0,session["graph"].size):
            print(retVal[i][j],end=" ")
        print()
    if retVal == None:
        return {"pos": False}
    else:
        return {"pos": True, "Matrix": retVal}

@app.route('/Adjlist', methods=['POST'])
def adjl():
    retVal=[]
    retVal = session["graph"].adjlist()
    if retVal == None:
        return {"pos": False}
    else:
        return {"pos": True, "List": retVal}



@app.route('/graph/<int:nodes>')
def graph(nodes):
    G = nx.complete_graph(nodes)
    nx.draw(G)

    img = BytesIO() # file-like object for the image
    plt.pyplot.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.pyplot.clf() # clear pyplot

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(threaded=True, port=5000)

