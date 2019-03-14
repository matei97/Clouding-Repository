import http.server
import socketserver
import json
import pyodbc
from urllib.parse import urlparse

Connection_string = r'Driver={SQL Server};Server=localhost;Database=Clouding;Trusted_Connection=yes;'


def deleteStudentById(id):
    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute(
        "DELETE FROM Students where id=" + id)
    cnxn.commit()


def getStudentsById(id):
    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute(
        "SELECT id,first_name,last_name,email,added FROM Students where id=" + id)
    row = cursor.fetchone()
    if not row:
        return dict()

    student = dict()
    student['id'] = row.id
    student['first_name'] = row.first_name
    student['last_name'] = row.last_name
    student['email'] = row.email
    student['added'] = row.added
    return student


def getAllStudents():
    toReturn = []
    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute(
        "SELECT id,first_name,last_name,email,added FROM Students")
    while True:
        row = cursor.fetchone()
        if not row:
            break
        student = dict()
        student['id'] = row.id
        student['first_name'] = row.first_name
        student['last_name'] = row.last_name
        student['email'] = row.email
        student['added'] = row.added
        toReturn.append(student)
    return toReturn


def saveStudent(json_body):
    if 'first_name' not in json_body or 'last_name' not in json_body or 'email' not in json_body:
        return 400
    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute("insert into Students(first_name, last_name,email) values (?, ?, ?)", json_body['first_name'],
                   json_body['last_name'], json_body['email'])
    cnxn.commit()
    cursor.execute(
        "SELECT id,first_name,last_name,email,added FROM Students order by id desc")
    row = cursor.fetchone()

    student = dict()
    student['id'] = row.id
    student['first_name'] = row.first_name
    student['last_name'] = row.last_name
    student['email'] = row.email
    student['added'] = row.added
    return student


def updateStudent(json_body, id):
    if 'first_name' not in json_body or 'last_name' not in json_body or 'email' not in json_body:
        return 400
    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute("UPDATE  Students SET first_name=?,last_name=?,email=? where id=?", json_body['first_name'],
                   json_body['last_name'], json_body['email'], id)
    cnxn.commit()
    cursor.execute(
        "SELECT id,first_name,last_name,email,added FROM Students where id=" + id)
    row = cursor.fetchone()

    student = dict()
    student['id'] = id
    student['first_name'] = row.first_name
    student['last_name'] = row.last_name
    student['email'] = row.email
    student['added'] = row.added
    return student


def patchStudent(json_body, id):
    if len(json_body) > 1 or (
            'first_name' not in json_body and 'last_name' not in json_body and 'email' not in json_body):
        return 400

    cnxn = pyodbc.connect(Connection_string)
    cursor = cnxn.cursor()
    cursor.execute("UPDATE  Students SET " + list(json_body.keys())[0] + "=? where id=?", list(json_body.values())[0],
                   id)
    cnxn.commit()
    cursor.execute(
        "SELECT id,first_name,last_name,email,added FROM Students where id=" + id)
    row = cursor.fetchone()

    student = dict()
    student['id'] = id
    student['first_name'] = row.first_name
    student['last_name'] = row.last_name
    student['email'] = row.email
    student['added'] = row.added
    return student


class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if "/students" in self.path:
            o = urlparse(self.path)
            params = str(o.query).split("=")
            if params[0] == 'id' and params[1].isdigit():
                value = getStudentsById(params[1])
                if len(value.items()) == 0:
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    return
                else:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(value).encode())
                    return
            elif len(params[0]) > 0:
                self.send_response(405)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return
            list = getAllStudents()
            if len(list) > 0:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(list).encode())
                return
        else:
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            return

    def do_POST(self):
        if "/students" in self.path:
            o = urlparse(self.path)
            params = str(o.query).split("=")
            if len(params[0]) > 0:
                self.send_response(405)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return

            content_len = int(self.headers.get('Content-Length'))
            if content_len == 0:  # nu avem nimic in body
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return
            response = self.rfile.read(content_len)
            json_body = json.loads(response.decode('UTF-8'))
            return_val = saveStudent(json_body)
            if return_val == 400:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
            else:
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(return_val).encode())
        else:
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

    def do_DELETE(self):
        if "/students" in self.path:
            o = urlparse(self.path)
            params = str(o.query).split("=")
            if params[0] == 'id' and params[1].isdigit():
                value = getStudentsById(params[1])
                if len(value.items()) == 0:
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    return
                else:
                    deleteStudentById(params[1])
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    return
            elif len(params[0]) > 0:
                self.send_response(405)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
        else:
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

    def do_PUT(self):
        if "/students" in self.path:  # daca avem ruta students
            o = urlparse(self.path)
            params = str(o.query).split("=")
            if params[0] == 'id' and params[1].isdigit():  # daca parametrul e id si valoarea e numerica
                value = getStudentsById(params[1])
                if len(value.items()) == 0:  # daca id-ul introdus nu corespunde niciunul student
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    return
                else:  # id-ul introdus e bun citim din body obiectul
                    content_len = int(self.headers.get('Content-Length'))
                    if content_len == 0:  # nu avem nimic in body
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        return

                    response = self.rfile.read(content_len)
                    json_body = json.loads(response.decode('UTF-8'))
                    return_val = updateStudent(json_body, params[1])
                    if return_val == 400:  # daca obiectul nu are toate atributele studentului
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                    else:  # returnam obiectul dupa update
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(return_val).encode())
                        return
            elif len(params[0]) > 0:  # daca avem mai multi parametri in url
                self.send_response(405)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return
            # alt parametru in url (idd,ide etc)
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
        else:  # daca nu avem students in url
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

    def do_PATCH(self):
        if "/students" in self.path:  # daca avem ruta students
            o = urlparse(self.path)
            params = str(o.query).split("=")
            if params[0] == 'id' and params[1].isdigit():  # daca parametrul e id si valoarea e numerica
                value = getStudentsById(params[1])
                if len(value.items()) == 0:  # daca id-ul introdus nu corespunde niciunul student
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    return
                else:  # id-ul introdus e bun, citim din body obiectul
                    content_len = int(self.headers.get('Content-Length'))
                    if content_len == 0:  # nu avem nimic in body
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        return

                    response = self.rfile.read(content_len)
                    json_body = json.loads(response.decode('UTF-8'))
                    return_val = patchStudent(json_body, params[1])
                    if return_val == 400:  # daca obiectul nu are toate atributele studentului
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                    else:  # returnam obiectul dupa update
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(return_val).encode())
                        return
            elif len(params[0]) > 0:  # daca avem mai multi parametri in url
                self.send_response(405)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                return
            # alt parametru in url (idd,ide etc)
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
        else:  # daca nu avem students in url
            self.send_response(405)
            self.send_header("Content-Type", "application/json")
            self.end_headers()


if __name__ == "__main__":
    PORT = 31338

    Handler = CORSHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
