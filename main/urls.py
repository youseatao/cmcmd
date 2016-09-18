from django.conf.urls import url
import views
urlpatterns = [
	url(r"^$", views.mainpage),
	url(r"^submit$", views.submit),
	url(r"^wait$", views.wait),
]

