from django.utils.decorators import method_decorator
from django.urls import path
from home.views import SignUpView, IndexView, LoginView, PostView, LogoutView, DetailView, DeletesView

urlpatterns = [
    path('', IndexView.as_view(), name="homepage"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('log_in', LoginView.as_view(), name="log_in"),
    path('log_out', LogoutView.as_view(), name="log_out"),
    path('posts', PostView.as_view(), name="posts"),
    path('details', DetailView.as_view(), name="details"),
    path('<int:id>/delete', DeletesView.as_view(), name='delete')
]