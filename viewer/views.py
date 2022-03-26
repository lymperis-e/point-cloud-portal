# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import RawSQL
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from viewer.models import Cloud


def home(request):
    user_clouds = get_user_clouds(request.user)
    from django.contrib.staticfiles.storage import staticfiles_storage
    import json
    import requests
    for cloud in user_clouds:
        url = "http://0.0.0.0:8000" + staticfiles_storage.url('pointclouds/{}/metadata.json'.format(cloud['file_name']))
        doc = requests.get(url)
        
        point_count = int(json.loads(doc.content)['points'])
        point_count = "{:,}".format(point_count)

        cloud['point_count'] = str(point_count)

    return render(request, 'index/index.html', {"clouds": user_clouds} )





def cesium_viewer(request, slug):
    cloud = Cloud.objects.get(file_name=slug)

    print(type(cloud))

    from django.contrib.staticfiles.storage import staticfiles_storage
    import json
    import requests
    url = "http://0.0.0.0:8000" + staticfiles_storage.url('pointclouds/{}/metadata.json'.format(str(cloud.file_name)))
    metadata = requests.get(url)
    bbox = json.loads(metadata.content)['boundingBox']
    midpoint = {"x": float(bbox['max'][0]) - float(bbox['min'][0]),
                "y": float(bbox['max'][1]) - float(bbox['min'][1]),
                "z": float(bbox['max'][2]) - float(bbox['min'][2])}




    return render(request, 'viewer/cesium_viewer.html', {"cloud": cloud, "midpoint": midpoint} )

def viewer(request, slug):
    cloud = Cloud.objects.get(file_name=slug)
    return render(request, 'viewer/viewer.html', {"cloud": cloud} )


def demo(request, slug):
    if slug == 'grand_canyon':
        return render(request, 'demo/grand_canyon.html')
    elif slug=='retz':
        return render(request, 'demo/retz.html')


# Map portal view

def map_viewer(request):
    return render(request, 'map_portal/map_portal.html')



# REturn a user's clouds as JSON, to feed into the map portal
def user_clouds_json(request):
    from django.db import connection
    from django.http import HttpResponse
    user = request.user
    with connection.cursor() as cursor:
        cursor.execute(" SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json)) FROM (SELECT * FROM public.viewer_cloud WHERE id IN (SELECT cloud_id FROM public.viewer_cloud_users WHERE customuser_id = %s)) AS t(location);", [user.id])
        #row = cursor.fetchone()
        resp = dictfetchall(cursor)
    resp = resp[0]['json_build_object']
    resp = str(resp).replace("'", '''"''')
    return HttpResponse(resp, content_type='application/json')






# Retrieve all the clouds that a user has permission to view
def get_user_clouds(user):
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.viewer_cloud WHERE id IN (SELECT cloud_id FROM public.viewer_cloud_users WHERE customuser_id = %s)", [user.id])
        #row = cursor.fetchone()
        resp = dictfetchall(cursor)
    return resp
    

# REturn all rows from a db cursor as a dict
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]