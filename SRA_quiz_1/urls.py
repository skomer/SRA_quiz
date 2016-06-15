from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^check_email/', views.check_email, name='check_email'),




	# url(r'^add_answer/', views.add_answer, name='add_answer'),
	# url(r'^user_dash/', views.user_dash, name='user_dash'),

]