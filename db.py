# coding: utf-8

import dataset

db = dataset.connect('sqlite:///videos.db')
videos = db['videos']
