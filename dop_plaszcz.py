from csv import reader, writer
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import numpy as np


def read_csv(name, nl="\n", dl=","):
    cloud=[]
    with open(name,newline=nl) as csvfile:
        csvreader = reader(csvfile, delimiter = dl)
        for xx, yy, zz in csvreader:
            cloud.append([float(xx), float(yy), float(zz)])
    return cloud

def write_csv(file_name, cloud_points):
    with open(file_name, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points:
            csvwriter.writerow(p)

cloud = read_csv("cylinder.xyz")

clusterer = KMeans(n_clusters=3)
X = np.array(cloud)
y_pred = clusterer.fit_predict(X)

red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

r = []
b = []
c = []

for i in range(len(cloud)):
    if red[i]:
        r.append(cloud[i])
    elif blue[i]:
        b.append(cloud[i])
    elif cyan[i]:
        c.append(cloud[i])
    else:
        print(cloud[i])

write_csv("cloud_r.xyz", r)
write_csv("cloud_b.xyz", b)
write_csv("cloud_c.xyz", c)
