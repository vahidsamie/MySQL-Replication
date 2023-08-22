from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection parameters
mysql_config = {
    'host': '10.1.1.3',
    'user': 'root',
    'password': 'yourpassword',
    'database': 'UserInfo'
}

@app.route('/API/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor(dictionary=True)
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
