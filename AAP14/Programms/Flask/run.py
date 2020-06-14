from flaskblog import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
    