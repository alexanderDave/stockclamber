#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:36:37 2020

@author: yuhandai
"""

import json,requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from pylab import *
import datetime
import operator

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn import svm,datasets


def createDate(a,b):
    np.random.seed(10)
    pointsPerCluster = float(a)/b
    x = []
    y = []
    for i in range(b):
        incomeCentroid = np.random.uniform(20000.0,200000.0)
        ageCentroid = np.random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0)])
            y.append(i)
    x = np.array(x)
    y = np.array(y)
    return x,y

def createDate2(a,b):
    np.random.seed(10)
    pointsPerCluster = float(a)/b
    x = []
    for i in range(b):
        incomeCentroid = np.random.uniform(20000.0,200000.0)
        ageCentroid = np.random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0)])
    x = np.array(x)
    return x


date = createDate2(100,4)
model = KMeans(n_clusters=4)
model = model.fit(scale(date))
#plt.scatter(date[:,0],date[:,1],c=model.labels_.astype(float))


(x,y) = createDate(100,5)
#plt.scatter(date[:,0],date[:,1],c=model.labels_.astype(float))
C=1.0
svc = svm.SVC(kernel='linear',C=C).fit(x,y)

def plotsvm(clf):
    xx,yy = np.meshgrid(np.arange(0,250000,100),np.arange(10,70,0.5))
    Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
    plt.figure()
    z = Z.reshape(xx.shape)
    plt.contourf(xx,yy,z,cmap=plt.cm.Paired,alpha=0.8)
    plt.scatter(x[:,0],x[:,1],c=y.astype(np.float))
    
plotsvm(svc)
plt.savefig('cu.png',format='png')
#plt.show()















