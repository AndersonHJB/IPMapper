from flask import Flask, request, jsonify
import requests
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://blog.bornforthis.cn", "http://127.0.0.1:4000"]}})

def get_geo_info(ip):
    # 使用免费API获取地理位置信息
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=zh-CN")
    data = response.json()
    if data['status'] == 'fail':
        return None

    # 解析并返回数据
    geo_info = {
        "ip": ip,
        "continent": data.get("continent", ""),
        "country_english": data.get("country", ""),
        "country": data.get("country", ""),
        "prov": data.get("regionName", ""),
        "city": data.get("city", ""),
        "district": data.get("district", ""),
        "isp": data.get("isp", ""),
        "lat": str(data.get("lat", "")),
        "lng": str(data.get("lon", "")),
        "area_code": data.get("region", ""),
        "city_code": data.get("city", ""),
        "elevation": "",
        "time_zone": data.get("timezone", ""),
        "weather_station": "",
        "zip_code": data.get("zip", "")
    }
    return geo_info

@app.route('/get_ip_info', methods=['GET'])
def get_ip_info():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"code": 400, "msg": "IP地址不能为空", "data": {}})

    geo_info = get_geo_info(ip)
    if not geo_info:
        return jsonify({"code": 404, "msg": "无法获取地理位置信息", "data": {}})

    return jsonify({
        "code": 200,
        "data": geo_info,
        "msg": "success",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "AI悦创·API：ip.bornforthis.cn"
    })


@app.route('/Local', methods=['GET'])
def get_local_ip_info():
    # 获取客户端的IP地址
    ip = request.remote_addr
    geo_info = get_geo_info(ip)
    if not geo_info:
        return jsonify({"code": 404, "msg": "无法获取地理位置信息", "data": {}})

    return jsonify({
        "code": 200,
        "data": geo_info,
        "msg": "success",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "AI悦创·API：ip.bornforthis.cn"
    })

if __name__ == '__main__':
    app.run(debug=True)
