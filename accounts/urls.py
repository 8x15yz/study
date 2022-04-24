from django.urls import path
from .views import index_to_comment

app_name = 'accounts'
urlpatterns = [
    path('forAnonymousUser/', index_to_comment.forAnonymousUser, name='forAnonymousUser'),
    path('userindex/', index_to_comment.userindex, name='userindex'),
    path('signup/', index_to_comment.signup, name='signup'),
    path('login/', index_to_comment.login, name='login'),
    path('logout/', index_to_comment.logout, name='logout'),
    path('profile/<str:username>/', index_to_comment.profile, name='profile'),
    path('create/', index_to_comment.create, name='create'),
    path('profile/<str:username>/retrieve/<int:p_pk>/', index_to_comment.retrieve, name='retrieve'),

    # 댓글로직
    path('profile/<str:username>/retrieve/<int:p_pk>/comments/', index_to_comment.comments_create, name='comments_create'),

]