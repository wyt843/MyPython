# 网络编程
- 网络协议：TCP/IP、UDP
- Socket 编程
# UDP编程
    - Server端流程
        - 建立socket,socket是负责具体通讯的一个实例
        - 绑定，为创建的scoket指定固定的端口和IP
        - 接受client发送的内容
        - 给对client发送反馈，此步骤为非必须步骤
    - Client 端流程
        - 1.建立socket
        - 2.发送内容到server
        - 3.接受server的反馈内容
    - 案例
        - Server 01.py
        - Client 02.py
# TCP 编程 面向连接的传输
    - Server 端流程：
        - 1、建立scoket
        - 2、绑定ip和port
        - 3、监听接入的访问scoket
        - 4、接受访问的socket，可以解释接受访问建立了一个通讯的连接
        - 5、接受对方的发送内容，利用接受的socket接受内容
        - 6、如果有必要，给对方发反馈信息
        - 7、关闭连接桐庐
    - Client 端流程：
        - 1、建立socket
        - 2、连接对方，请求跟对方建立通路
        - 3、发送内容到服务器
        - 4、接受反馈
        - 5、关闭连接通路
    - 案例
        - Server 03.py
        - Client 04.py
# FTP 编程
    - FTP文件传输协议
    - 用途：定义的一些特殊的上传、下载文件的服务
    - 用户分类：登录FTP服务器必须有一个账户
        - Real账户：注册账户
        - Guest账户:可能临时针对某类人授权的账户
        - Anonymous账户：匿名账户，允许任何人访问
    - FTP 流程：
        - 1、客户端 连接ftp服务器
            `f = ftplib.FTP()
             f.connect(HOST)`
        - 2、客户端输入用户名、密码
            `f.login()`
        - 3、客户端 操作ftp服务器 文件操作
            `f.cwd(DIR) # 更改目录
             f.retrbinary("RETR {0}".format(FILE),open(FILE,'wb').write())  #下载文件到本地
            `
        - 4、客户端 连接关闭
            `f.close()
            `
    - FTP 文件表示：
        - 分三段表示ftp上的文件
        - host:主机，类似于：ftp.mozilla.org
        - DIR:目录
        - File

    - 案例 05.py

# Mail 编程
- SMTP发送邮件协议
    - 构造邮件文本
        - mail["From"] :发送人地址
        - mail["To"]：接受人地址
        - mail["Subject"]:邮件主题
    - 连接邮件服务器
    - 登录
    - 发送(发件人，收件人，邮件内容)
- 案例 06.py
- 带附件的案例 07.py
- 同时支持html和text格式
    - 构建一个MIMEMultipart格式邮件
    - MIMEMultipart的subtype设置为alternative格式
    - 添加HTML和TEXT格式邮件
    - 案例08.py

- POP3 接受邮件协议
    - 步骤：
        - 用poplib下载邮件结构体原始内容
            - 1、准备相应内容（邮箱地址，密码，pop3实例）
            - 2、身份认证
            - 3、一般会先得到邮箱内 邮件的整体列表
            - 4、根据相应序号，得到某一封邮件的邮件结构体
            - 5、 利用解析函数进行解析出相应的邮件结构体
        - 用email解析邮件
        - 案例 09.py
- HTTP 协议
