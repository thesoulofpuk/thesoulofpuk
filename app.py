# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:40:50 2020

@author: ASUS
"""
import keras
import tensorflow
import numpy as np
from PIL import Image, ImageOps
from botnoi import scrape as sc
from botnoi import cv
import os
import botnoi as bn
import pickle
import pandas as pd
import numpy as np
import flask
from flask import Flask,redirect, url_for, request
from flask_restful import Resource, Api, reqparse
import requests

app = flask.Flask(__name__,template_folder='templates')
api = Api(app)

with open(f'finalized_model.sav', 'rb') as f:
    mod = pickle.load(f)

def import_and_predict(image_url,mod):
        a = cv.image(image_url)
        feat = a.getresnet50()
        prediction = mod.predict([feat])
        return prediction 


@app.route('/',methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('loginurl.html'))

    if flask.request.method == 'POST':
        # Extract the input
        url = flask.request.form['URL']

        predictioning = import_and_predict(url,mod)

        return flask.render_template('loginurl.html',
                                     original_input={'URL':url},
                                     result=predictioning,
                                     )




if __name__ == '__main__':
    app.run()
#mod = tf.keras.models.load_model('mymod.mod')
#file = input("Please input url")    
#image = file
#import_and_predict(image, mod)