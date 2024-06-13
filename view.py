import json
import requests
import urllib3
from flask import request, Blueprint, render_template

urllib3.disable_warnings()

path = Blueprint('path', __name__)


@path.route('/index', methods=['GET', "POST"])
def index():
    return render_template("index.html")


@path.route('/post_form', methods=['POST', ])
def post_form():

    url = 'https://www.oscs1024.com/oscs/v1/intelligence/list';

    data = {
        'page': int(request.form.get('page', 1)),
        'per_page':int(request.form.get('per_page',10)),
    }
    res = requests.post('https://www.oscs1024.com/oscs/v1/intelligence/list',  json=data).json()
    rows = res['data']['data']
    for i in rows:
        idx = rows.index(i)
        rows[idx]['created_at'] = i['created_at'].replace('T', ' ').replace('+', ' ')[0:20]
   
    respos = {
        "status": 0,
        "data": {
            'rows': rows,
            "count": res['data']['total']
        },
        'msg': ''
    }
    return json.dumps(respos)

@path.route('/detail', methods=['GET' ])
def detail():
    mps = request.args.get('id')
  


  
    json_data = {
        'vuln_no': mps,
    }

    res = requests.post('https://www.oscs1024.com/oscs/v1/vdb/info',  json=json_data).json()

    rows = res['data'][0]

    effect = ''
    url = ''
    for i in rows['references']:
        url += i['url']+"\r\n" 
    rows['url'] =url
    for i in rows['effect']:
        effect += i['name']+'@'+str(i['affected_version'])+"\r\n\n\n\r\t"
    rows['effect'] = effect


    respos = {
        "status": 0,
        "data":rows,
        'msg': ''
    }
    return json.dumps(respos)
