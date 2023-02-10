from django.shortcuts import render
from django.http import HttpResponse


def scrap_here(request):
    return HttpResponse('이 함수에서 스크래핑 하시고 결과 반환하면 됩니다')