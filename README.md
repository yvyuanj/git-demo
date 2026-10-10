# git-demo — Django 初学项目

一个用于学习 Django 的入门 Web 项目（作业练习），包含用户管理、管理员增删改查、登录验证、天气查询、ORM 增删改查、模板渲染等功能示例。
# git-demo

## 使用技术
- 编程语言：Python3
- Web框架：Django
- 前端：HTML、Bootstrap、JavaScript
- 数据库：SQLite3

## 功能模块
1. 用户信息管理：实现用户的新增、查询、修改、删除
2. ORM数据库操作：使用Django ORM完成数据表增删改查演示
3. 用户登录验证：账号密码校验，登录状态保存
4. 模板渲染：Django模板继承，动态数据渲染到HTML页面
5. 天气查询页面：简易页面展示示例
6. Admin后台管理：Django自带后台，可视化管理数据

## 数据模型
- UserInfo 用户表：存储用户名、账号、所属部门、角色等信息
- Department 部门表：保存部门名称信息
- Role 角色表：定义用户角色类型，区分权限


## 技术栈

- Python 3.x
- Django 6.1
- MySQL（数据库连接配置见 `site2/site1/settings.py`）
- Bootstrap 3 / jQuery（前端样式）
- pymysql、requests

## 项目结构

```
site2/
├── manage.py          # 项目管理入口
├── site1/             # 项目配置（settings / urls / wsgi 等）
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── app01/             # 业务应用
    ├── views.py       # 视图函数
    ├── models.py      # ORM 数据模型
    ├── templates/     # 页面模板
    ├── static/        # 静态资源（CSS / JS / Bootstrap）
    └── migrations/    # 数据库迁移
```

## 环境准备
### 1. 环境要求
Python >=3.8，安装Django框架

### 2. 克隆项目
```bash
git clone https://github.com/yvyuanj/git-demo.git
cd git-demo
创建虚拟环境：
python -m venv venv
# Windows激活虚拟环境
venv\Scripts\activate

## 功能模块

- 用户信息管理：新增 / 列表 / 删除（基于 ORM）
- 管理员管理：新增 / 列表 / 删除（基于 pymysql 操作 MySQL）
- 登录验证：示例登录页
- 天气查询：调用 Open-Meteo 接口获取实时温度
- ORM 增删改查练习
- 模板渲染：模板语法与变量传递示例

## 运行方式

1. 按 `site2/site1/settings.py` 配置好本地 MySQL 连接（库名 / 账号 / 密码）。
2. 进入项目目录并启动服务：

```bash
cd site2
python manage.py runserver
```

3. 浏览器访问 http://127.0.0.1:8000/ 查看效果。

> 说明：本仓库为 Django 学习作业示例，数据库账号密码等配置仅用于本地开发环境。
