# JSON
- 在线工具
    - https://www.sojson.com
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
- JSON(JavaScriptObjectNotation）
- 轻量级的数据格式，基于ECMAScript
- json 格式是键值对的形式的数据集
    - key: 字符串
    - value： 字符串,数字,列表，json
    - json 使用大括号包括
    - kv用逗号隔开
    `
     ManagerList = [
        {"name": "tom", "age": "27", "set": "F"},
        {"name": "joy", "age": "37", "set": "M"},
        {"name": "rub", "age": "23", "set": "F"}
      ]
    `
- json 和 python格式的对应
    - 字符串：字符串
    - 数字：数字
    - 队列： list
    - 对象：dict
    - 布尔值：布尔值
- python for json
    - json 包
    - json 和python对象的转化集
        - json.dumps():对数据编码，把python格式转化为json
        - json.loads():对数据解析，把json转化为python格式
    - python读取json文件
        - json.dump():把json写入文件
        - json.load():从文件读取json内容
    - 案例 01.py
    - 读取文件案例 02.py