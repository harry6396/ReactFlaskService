import json
from flask_cors import CORS
import DatabaseConnectionFile
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)

# to get the user details for the login


@app.route("/api/GetSongsData")
def GetSongsData():

    # to establish a connection between DB
    databaseConnection = openDatabaseConnection()
    dataFetcher = databaseConnection.cursor()
    query = "SELECT * FROM SongDetails ORDER BY Rank";

    dataFetcher.execute(query)

    myresult = dataFetcher.fetchall()

    iCounter=0
    data={}

    for doc in myresult:
        data[iCounter] = doc
        iCounter = iCounter + 1

    return jsonify(json.dumps({'status':data}))


@app.route("/api/GetSongsData/<string:searchKeyWord>")
def GetSearchedSongsData(searchKeyWord):

    ## to establish a connection between DB
    databaseConnection = openDatabaseConnection()
    dataFetcher = databaseConnection.cursor()
    query = "SELECT * FROM SongDetails WHERE (ARTISTS LIKE '%"+searchKeyWord+"%' OR NAME LIKE '%"+searchKeyWord+"%') ORDER BY RANK"

    dataFetcher.execute(query)

    myresult = dataFetcher.fetchall()
    iCounter=0
    data={}

    for doc in myresult:
        data[iCounter] = doc
        iCounter = iCounter + 1

    return jsonify(json.dumps({'status':data}))


@app.route("/api/AddSong", methods=['POST'])
def AddSong():

    req = request.get_json()
    # to establish a connection between DB
    databaseConnection = openDatabaseConnection()
    dataPusher = databaseConnection.cursor()
    dataPusher.execute('''INSERT INTO SongDetails (name,artists,duration_ms) VALUES(%s, %s, %s)''', (req['songName'],
                                                                                                     req['songArtist'],
                                                                                                     req['songDuration']
                                                                                                     ))
    databaseConnection.commit()
    return "Done"


def openDatabaseConnection():
    # Uncomment when running on localhost
    # configuration = DatabaseConnectionFile.Configuration('http://localhost:3306/', 'root', 'harry', 'SongsCollection')

    # Comment when running on localhost
    configuration = DatabaseConnectionFile.Configuration('mysongcollection.cg11qeviywl5.us-east-2.rds.amazonaws.com'
                                                         ,'harry6396','prabhat1','harry6396')

    return DatabaseConnectionFile.connectDB(configuration)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)





