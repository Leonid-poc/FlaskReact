from flask import Flask, request
import psycopg2 as psg

conn = psg.connect(database="delivery_base", user='postgres', password='1234')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/members')
def members():
    return {"Members": ["Member1", "Member2", "Member3"]}

@app.route('/register', methods=['POST'])
def register():
    req = request.get_json()
    print(req)
    cursor.execute("SELECT * FROM users WHERE email = %s", ( req['email'], ))
    conn.commit()
    resp_user = cursor.fetchone()
    if resp_user is None:
        cursor.execute("INSERT INTO users (name, surname, email, password, number) VALUES (%s, %s, %s, %s, %s)",
                       (req['name'], req['surname'], req['email'], req['password'], req['tel']))
        conn.commit()
        return {"Message": "Success"}
    
    return {"Message": "User already exists"}

if __name__ == '__main__':
    app.run(debug=True)
    cursor.close()
    conn.close()

# /var/lib/pgsql/data/pg_hba.conf --> (peer -> md5)