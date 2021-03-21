from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader, RequestContext


# Create your views here.


# def index(request):
#     """dsa"""
#     # return HttpResponse("success")
#
#     # 1.加载模板文件
#     template = loader.get_template("booktest/index.html")
#
#     # 2.定义模板上下文，给模板文件传递数据
#     context = {"result": True, "code": 200}
#
#     # 3.模板渲染：产生标准html内容
#     # res_html = template.render(res_data, request=request)
#
#     # 4.返回给浏览器
#     return render(request, "booktest/index.html", context)


def my_render(request):
    html_path = "booktest/index.html"
    context = {"data": list(range(1, 10))}
    return render(request, html_path, context)
