# IPMapper

你好，我是悦创。

根据 IP 地址获取地理位置信息。

这是一个基于Flask的开源IP地址地理位置查询 API，可以部署在 GitHub、Vercel 或其他服务器上。

## 部署到Vercel

你可以点击下面的按钮一键部署此项目到Vercel。

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/AndersonHJB/IPMapper&project-name=ipmapper&repo-name=IPMapper)

以下是按照你的要求编写的API说明文档，包括请求参数说明、返回示例、返回参数说明等内容：

---

## 请求说明

### 参数说明

| 接口地址                                     | 请求方法 | 返回格式 |
| -------------------------------------------- | -------- | -------- |
| `https://api.bornforthis.cn/api/ip-location` | `GET`    | `JSON`   |

### 请求参数说明

| 名称 | 必填 |  类型  |  说明   |
| :--: | :--: | :----: | :-----: |
|  ip  |  是  | string | IP 地址 |

### 返回示例

```json
{
  "code": 200,
  "data": {
    "ip": "112.51.213.94",
    "continent": "",
    "country": "中国",
    "country_english": "中国",
    "prov": "福建省",
    "city": "莆田市",
    "district": "",
    "isp": "China Mobile",
    "lat": "25.4536",
    "lng": "118.9929",
    "area_code": "FJ",
    "city_code": "莆田市",
    "elevation": "",
    "time_zone": "Asia/Shanghai",
    "weather_station": "",
    "zip_code": ""
  },
  "msg": "success",
  "source": "AI悦创·API：api.bornforthis.cn",
  "time": "2024-08-21 11:45:05"
}
```

### 返回参数说明

|      名称      |  类型   |       说明       |
| :------------: | :-----: | :--------------: |
|      code      | string  |      状态码      |
|      data      | object  |   结果数据对象   |
|      ip        | string  |      IP地址      |
| data.continent | string  |       大洲       |
|  data.country  | string  |       国家       |
| data.country_english | string | 国家英文名称 |
|   data.prov    | string  |       省份       |
|   data.city    | string  |       城市       |
| data.district  | string  |       区县       |
|    data.isp    | string  | 互联网服务提供商 |
|    data.lat    | string  |       纬度       |
|    data.lng    | string  |       经度       |
| data.area_code | string  |     区域代码     |
| data.city_code | string  |     城市代码     |
| data.elevation | string  |     海拔高度     |
| data.time_zone | string  |       时区       |
| data.weather_station | string | 天气站代码  |
|  data.zip_code | string  |     邮政编码     |
|      msg       | string  |     返回消息     |
|     source     | string  |     数据来源     |
|      time      | string  |     响应时间     |

### 示例请求

```plaintext
https://ip.bornforthis.cn/get_ip_info?ip=112.51.213.94
```

这个文档结构清晰地展示了API的使用方法，包括如何发送请求、返回数据的结构和每个字段的含义。

## 开发

本项目还在持续优化中，欢迎点击 Star，你的 Star 是我最大的鼓励！

## 建议

如果私人使用，则建议把请求头限制成自己的域名，可以防止恶意调用。

```python
# 指定域名/IP 访问
CORS(app, resources={r"/*": {"origins": ["https://blog.bornforthis.cn", "http://127.0.0.1:4000"]}})

# 允许任何来源访问
CORS(app, resources={r"/*": {"origins": "*"}})
```