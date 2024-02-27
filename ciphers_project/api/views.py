from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import caesar_encode

def greetings(request):
    result = {"message" : "Welcome to ciphers service!"}
    return JsonResponse(result)

def encode(request, plain_text, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caesar_encode(plain_text, shift)
    return JsonResponse({"cipher": cipher})
