# -*- coding = utf-8 -*-
# @Time : 2022/6/30 16:25
# @Author : Iscolito
# @File : map.py
# @Software : PyCharm
import folium
import pandas as pd
import json
df=pd.read_excel("D:\data\list.xls")
latitude=34.15
longitude=109.32
lantian_map=folium.Map(location=[latitude,longitude],zoom_start=12)
folium.Marker(
    location=[latitude,longitude],
    popup='蓝田县',
    icon=folium.Icon(icon='cloud')
).add_to(lantian_map)
url='https://geo.datav.aliyun.com/areas_v3/bound/geojson?code=610122'
san_lantian=f'{url}'
folium.GeoJson(
    san_lantian,
    style_function=lambda feature: {
        'fillColor': '#ffff00',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'
}
).add_to(lantian_map)

for i in range(df.shape[0]):
    folium.Marker(
        location=[float(df.values[i,1]),float(df.values[i,2])],
        popup="<<"+df.values[i,0]+">>\n"+"联系电话:"+"<<"+str(df.values[i,3])+">>",
        icon=folium.Icon(icon='info-sign',color='green')
    ).add_to(lantian_map)

    folium.Circle(
        radius=400,
        location=[float(df.values[i,1]),float(df.values[i,2])],
        popup="基本信息：",
        color='blue',
        fill=True,
        fill_color='#3186cc',
).add_to(lantian_map)
lantian_map.add_child(folium.ClickForMarker(popup='标记点'))
lantian_map.save('map.html')