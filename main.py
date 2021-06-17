from logging import debug
from warnings import catch_warnings
from flask import Flask, request
from werkzeug.datastructures import ContentSecurityPolicy
import requests
import json

app = Flask(__name__)

posts = []  #keep dict [post1, post2, post3]

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        
        body = request.get_json() #keep something user sent to python

        req = requests.get('https://api.thecatapi.com/v1/images/search')
        res_list = req.json()
        body['url'] = res_list[0]['url']

        for post in posts:
            if post['name'] == body['name']:
                body['url'] = post['url']
            else :
                body['url'] = res_list[0]['url']
       
        posts.append(body)
        return {"Message" : "Post already add to database", "body": body},201

    elif request.method == 'GET':
        
        user = request.args.get('user') #query user input
        if user != None:
            _posts = [] #keep user all post 
            for post in posts: #check post
                if post['name'] == user:
                    _posts.append(post)
            return {"posts" : _posts},200
        return {"posts" : posts},200

# endpoint /post
# GET user get data on database to SHOW on WEBPAGE
# GET >> query username >> return only user post
# POST user submit or post data to database


if __name__== '__main__':
    app.run(debug=True)