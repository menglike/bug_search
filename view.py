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
    vul_name = request.form.get('vul_name', '').strip()
    vul_num = request.form.get('vul_num', '').strip()
    app_name = request.form.get('app_name', '').strip()
    vul_level = request.form.get('vul_level', '').strip()

    url = 'https://api.liangmlk.cn/risk_bug.php';

    data = {
        'page': request.form.get('page', 1),
        "perPage": request.form.get('perPage', 20)
    }
    if vul_name:
        data['vul_name'] = vul_name
    if vul_num:
        data['vul_num'] = vul_num
    if vul_level:
        data['vul_level'] = vul_level
    if app_name:
        data['app_name'] = app_name

    res = requests.post(url, verify=False, data=json.dumps(data)).json()
    rows = res['data']['rows']
    for i in rows:
        idx = rows.index(i)
        rows[idx]['vul_name'] = i['vul_name'].replace('<i>', '[').replace('</i>', ']')
        rows[idx]['app_name'] = i['app_name'].replace('<i>', '[').replace('</i>', ']')
        if i['vul_level'] == 1:
            rows[idx]['vul_level'] = '低'
        if i['vul_level'] == 2:
            rows[idx]['vul_level'] = '中'
        if i['vul_level'] == 3:
            rows[idx]['vul_level'] = '高'

    respos = {
        "status": 0,
        "data": {
            'rows': res['data']['rows'],
            "count": res['data']['count']
        },
        'msg': ''
    }
    return json.dumps(respos)
