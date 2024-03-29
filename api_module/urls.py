"""
URL configuration for Email_campaign_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_module.controllers.userController import userControllerFunction
from api_module.controllers.contentController import ContentControllerFunction
from api_module.controllers.contentActionController import ContentAction
from api_module.controllers.kafkaController import exposeEndpoint

urlpatterns = [
    path('EnterUserData', userControllerFunction.as_view(), name = "EnterUserData"),            #endpoint for entering user data
    path('EnterUserContent', ContentControllerFunction.as_view(), name = "EnterUserContent"),   #endpoint for entering user content
    path('Unsubscribe', ContentAction.as_view(), name = "Unsubscribe"),                         #endpoint for unsubscribing
    path('envokeEmailer', exposeEndpoint.as_view(), name = "Emailer")                           #endpoint for sending email
]
