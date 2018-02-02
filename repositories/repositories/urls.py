from django import urls

from api import views


urlpatterns = [
        urls.path('repositories/<str:owner>/<str:repository_name>/',
                  views.RepositoriesView.as_view(),
                  name='repositories'),
]
