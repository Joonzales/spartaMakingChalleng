from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.cinema


#홈 화면 보여주기
@app.route('/')
def home():
    return render_template('home.html')


# 영화 랭킹 화면 보여주기
@app.route('/ranking')
def ranking():
    return render_template('Ranking.html')


# 이벤트 화면 보여주기
@app.route('/event/cgv')
def event_cgv():
   return render_template('Event_cgv.html')

@app.route('/event/lotte')
def event_lotte():
   return render_template('Event_lotte.html')

@app.route('/event/mega')
def event_mega():
   return render_template('Event_mega.html')


# 상영관 위치 화면 보여주기
@app.route('/map')
def map():
    return render_template('map.html')





# 영화 랭킹 데이터 가져오기
@app.route('/poster', methods=['GET'])
def listing_poster():
    poster_list = list(db.poster.find({}, {'_id': False}))
    return jsonify({'all_poster':poster_list})


# 이벤트 데이터 가져오기
@app.route('/cgv', methods=['GET'])
def listing_cgv():
    events = list(db.MovieMap_CGV.find({}, {'_id': False}))
    return jsonify({'cgv_all_events':events})

@app.route('/lotte', methods=['GET'])
def listing_lotte():
    events = list(db.MovieMaplotte.find({}, {'_id': False}))
    return jsonify({'lotte_all_events':events})

@app.route('/mega', methods=['GET'])
def listing_mega():
    events = list(db.MovieMapMega.find({}, {'_id': False}))
    return jsonify({'mega_all_events':events})


# 상영관 위치 데이터 가져오기
@app.route('/movie', methods=['GET'])
def movie():        
    theaters = list(db.theater.find({}, {'_id': False}))
    theaters_list = []
    for theater in theaters:      
        doc = {
            'name' : theater["name"][0],
            'Lat' : theater["name"][1],
            'Lng' : theater["name"][2]
        }        
        theaters_list.append(doc)
    return jsonify({'all_doc': theaters_list})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)