from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
# Create your views here.
# url: myapp/index
def index(request):
    return render(request, template_name='vue_demo.html')
# url: myapp/methond_get
@require_http_methods(["GET"])
def method_get(request):
    if request.method == 'GET':
        # 获取 get 参数
        print(request)
        print(request.GET['a'])
        print(request.GET['b'])
        # 返回 json 数据
        response = {}
        response['msg'] = 'success'
        response['error_num'] = 0
        response['method'] = 'GET'
        print(response)
        return JsonResponse(response)

