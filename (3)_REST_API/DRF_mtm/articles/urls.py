from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from . import views

schema_view = get_schema_view(
   openapi.Info(
        title="싸피 장고 REST API",
        default_version='v1',
        # 여기 아래부터는 선택 인자
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('cards/', views.card_list),
    path('cards/<int:card_pk>/', views.card_detail),
    path('<int:card_pk>/register/<int:article_pk>/', views.register),
    path('swagger/', schema_view.with_ui('swagger')),
]
