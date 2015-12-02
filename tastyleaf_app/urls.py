from django.conf.urls import patterns, url
import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^get-stories/$', views.getStories, name='get-stories'),
        url(r'^submit-story/$', views.submitStory, name='submit-story'),
        ]