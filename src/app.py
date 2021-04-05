from flask import Flask, render_template_string
import json
from db_handler import *
from helpers import readFile, manipulateData

app = Flask(__name__)


@app.route('/')
def userDetails():
    # displays a web page with user details, exported from MongoDB

    try:
        jsonData = json.loads(readFile(EXPORT_PATH))
    except Exception as e:
        return f"Could not find data file to read. Exception: {e}"

    return render_template_string('''
        <h1>User Details</h1>
        Welcome! Details exported from the MongoDB 'users' collection
        are displayed in this page. (sensitive info has been redacted)
        <br><br>Note: These details have been automatically exported
        into your machine at 'exportData/users.json'. <br><br>

        <table border="1">
            <thead>
                <tr>
                    {% for col in colnames %}
                    <th>{{ col }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for record in records %}
                <tr>
                    {% for col in colnames %}
                    <td>{{ record[col] }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>
        ''', records=jsonData, 
        colnames=['firstname', 'lastname', 'username', 'password'])


def main ():
    # main function - init mongo client, create db, create collection, inserts data
    # exports collection, manipulates file, an

    mongoClient = initMongoClient()
    mydb = createDbInMongo(mongoClient)
    mycol = createCollectionInMongo(mongoClient, mydb)
    insertDataFileIntoMongoCollection(mongoClient, mycol)
    exportCollectionToJson(mycol)
    manipulateData()
    app.run(host='0.0.0.0', debug=True, use_reloader=False)


# execute main
if __name__ == "__main__":
    main()