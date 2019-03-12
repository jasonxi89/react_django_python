# import json
# from django.shortcuts import render, HttpResponse
#
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import exceptions
#
#
# def users(request):
#     users_list = ['alex','oldBoy']
#     return HttpResponse(json.dumps((users_list)))
#
#
#
# from django.views import View
#
# # class MybasicView(object):
# #     def dispatch(self, request, *args, **kwargs):
# #         print("before")
# #         ret = super(MybasicView,self).dispatch(request, *args, **kwargs)
# #         print("after")
# #         return ret
# class mybaseview(object):
#     def dispatch(self,request, *args, **kwargs):
#         print("这就是套路")
#         ret = super(mybaseview, self).dispatch(request,  *args, **kwargs)
#         print("木有错")
#         return ret
#
# from django.utils.decorators import method_decorator
#
# class StudentsView(mybaseview,View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self,request, *args, **kwargs):
#         return super(StudentsView, self).dispatch(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         print("get方法")
#         return HttpResponse('GET方法')
#
#     def post(self,request, *args, **kwargs):
#         return HttpResponse('POST方法')
#
#     def put(self,request, *args, **kwargs):
#         return HttpResponse('PUT方法')
#
#     def delete(self,request, *args, **kwargs):
#         return HttpResponse('DELETE方法')
#
#
#
#
# ###############restful framework
# from rest_framework.views import APIView
#
#
# class MyAuthentication(object):
#     def authenticate(self,request):
#         token = request._request.GET.get('token')
#         #获取用户名和密码，去数据库校验
#         if not token:
#             raise exceptions.AuthenticationFailed('用户认证失败')
#         return ("alex",None)
#
#
#     def authenticate_header(self,val):
#         pass
#
#
# class Dogview(APIView):
#
#     authentication_classes = [MyAuthentication,]
#
#     def get(self, request, *args, **kwargs):
#         print("get方法")
#         ret = {
#             'code':1000,
#             'msg':'xxxx'
#         }
#         return HttpResponse(json.dump(ret),status=201)
#
#     def post(self,request, *args, **kwargs):
#         return HttpResponse('POST方法')
#
#     def put(self,request, *args, **kwargs):
#         return HttpResponse('PUT方法')
#
#     def delete(self,request, *args, **kwargs):
#         return HttpResponse('DELETE方法')

ORDER_DICT = {
    1:{
        'name':'媳妇',
        'age':18,
        'gender':'男'
    },
    2:{
        'name': '狗',
        'age': 15,
        'gender': '男'
    }
}


from django.shortcuts import  render
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from app01 import models
from rest_framework import exceptions
from rest_framework.request import Request
def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(user, encoding = 'utf-8')
    m.update = (bytes(ctime, encoding = 'utf-8'))
    return m.hexdigest()


class AuthView(APIView):


    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名密码错误'
            token  = md5(user)
            #存在更新，不存在就创建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
        except:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return  JsonResponse(ret)


class Authication(object):
    def authenicate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        #在rest framwork内部， 会将这两个字段赋值给request,以供以后使用
        return (token_obj.user,token_obj)

    def authenticate_header(self,request):
        pass

class OrderView(APIView):
    ##用于订单相关业务
    authentication_classes = [Authication,]
    def get(self, request, *args, **kwargs):
        # token = request._request.GET.get('token')
        # if not token:
        #     return HttpResponse('用户未登录')
        ret = {'code':1000, 'msg':None,'data':None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            ret = {
                'code':123,
                'msg':'不会错'
            }
        return JsonResponse(ret)


