from voting_app import app

if __name__=='__main__':
    app.run(debug=True)

    # wifi hosting
    # app.run(host='0.0.0.0', port='5000', debug=True, threaded=True)