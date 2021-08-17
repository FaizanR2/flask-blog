from website import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) # to change the port (default is 5000), add another parameter 'port=xxxx'
