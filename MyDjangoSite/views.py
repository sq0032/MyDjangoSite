
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import json
import os

def main(request):
    
    if 'RDS_HOSTNAME' in os.environ:
        env = 'AWS EB'
    else:
        env = 'LOCAL'

    return JsonResponse({'env':env, 'test':'AAA'})