from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pymysql
from django.shortcuts import render, redirect
from django.template.defaultfilters import title


def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    return render(request,'user_list.html')

def user_add(request):
    return render(request,'user_add.html')
def tpl(request):
    name = "韩超发方法"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name":"郭智", "salary":100000, "role":"CTO"}
    # 修正用户列表，严格三个不同的人
    user_list = [
        {"name":"李晋", "salary":100000,"role":"CEO"},
        {"name":"卢慧", "salary":100000, "role":"CEO"},
        {"name":"赵建先", "salary":100000, "role":"CEO"},
    ]
    msg="嘟嘟嘟"

    return render(request, 'tpl.html', {
        "n1": name,
        "n2": roles,
        "n3": user_info,
        "n4": user_list,
        "n5": msg,
    })

def weather(req):
    import requests
    res = requests.get('http://api.open-meteo.com/v1/forecast?latitude=30.67&longitude=104.07&current=temperature_2m')
    data_list = res.json()
    print(data_list)

    return render(req,'weather.html',data_list)
def something(request):
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    return redirect("http://www.baidu.com")
def login(request):
    if request.method == "GET":
        return render(request,"login.html")

    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == '123':
        return  redirect("http://www.chinaunicom.com.cn/")
    return render(request,"login.html",{"error_msg":"用户名或密码错误"})
# Create your views here.
def admin_list(request):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from admin")
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, "admin_list.html", {"data_list": data_list})

def admin_delete(request):
    del_id = request.GET.get("id")

    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor()
    cursor.execute("delete from admin where id=%s", del_id)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/admin_list/")
def admin_add(request):
    if request.method == "POST":
        print("全部POST数据：", request.POST) # 打印所有POST内容
        username = request.POST.get("username")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        print("username=", username, "password=", password, "mobile=", mobile)

        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user='root',
            password="Root@123456",
            charset='utf8',
            database='unicom'
        )
        cursor = conn.cursor()
        sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
        cursor.execute(sql, [username,password,mobile])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/admin_list/")
    return render(request, "admin_add.html")
from app01.models import Department,UserInfo
def orm(request):
    #Department.objects.create(title="财务部")
    #Department.objects.create(title="IT部")
    #Department.objects.create(title="运营部")
    #UserInfo.objects.create(name="武沛奇",password="123",age =18)
    #UserInfo.objects.create(name="朱虎飞",password="666",age =25)
    #UserInfo.objects.create(name="吴阳军",password="888")
    #获取数据
    #data_list=[对象，对象，对象]
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)
    # #data_list=[对象，]
    # data_list = UserInfo.objects.filter(id=1)
    # print(data_list)
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj,id,row_obj.name,row_obj.password,row_obj.age)
    #
    #
    #
    # return HttpResponse("成功")
    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(id=2).update(password=999)
    UserInfo.objects.filter(name="朱虎飞").update(age=999)
    return HttpResponse("成功")
def info_list(request):
    #1.获取数据库中所有用户信息
    #【对象，对象，对象】
    data_list = UserInfo.objects.all()
    #2.渲染模板，返回用户
    return render(request,"info_list.html",{"data_list":data_list})
def info_add(request):
    if request.method == "GET":
       return render(request,"info_add.html")
    #获取用户提交的数据
    user=request.POST.get("user")
    pwd=request.POST.get("pwd")
    age=request.POST.get("age")
    #添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)
    #自动跳转
    #return redirect("http://127.0.0.1:8000/info/list")
    return redirect("/info/list/")
def info_delete(request):
    nid = request.GET.get("id")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")

