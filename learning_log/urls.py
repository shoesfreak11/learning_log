"""
URL configuration for learning_log project.

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

# ******added by alain  30/11/2023 ******

from django.urls import path
#from . import views
from learning_logs.views import My_View

# To this import statement

#from learning_logs.views import My_View

urlpatterns = [
    
     path("learning_log/", My_View.as_view(), name="my_view"),
     #path("learning_log/", My_View.as_view(), name="my_view"),
     #path('', views.My_View, name="my_view"),  # FBV approach
     path('admin/', admin.site.urls),
]

# *******correction from Miracle******
#from django.urls import path
#from . import views
#
#urlpatterns = [
#    # path("learning_log/", My_View.as_view(), name="my_view")  # CBV approach, remember to have class imported
#    path('', views.My_View, name="my_view")  # FBV approach
#]