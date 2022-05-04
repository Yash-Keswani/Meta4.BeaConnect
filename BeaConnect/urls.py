"""Meta4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from BeaConnect import views

urlpatterns = [
	path('view_table/<str:table_name>', views.view_table),
	path('add_request', views.insert_request),
	path('new_request', views.new_request_page),
	
	path('call_volunteer', views.call_volunteer),
	path('elderly_home', views.elderly_home),
	path('feedback', views.feedback),
	path('requests', views.requests),
	path('volunteer_details', views.volunteer_details),
	path('volunteer_home', views.volunteer_home),

]
