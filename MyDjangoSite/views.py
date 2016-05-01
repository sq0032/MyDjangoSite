
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse



def main(request):
  return JsonResponse({'foo': 'aaa'})