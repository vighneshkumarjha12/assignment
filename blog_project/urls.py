from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from blog_app import views 
from django.conf import settings
from django.conf.urls.static import static # 👈 import your blog_list view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ API routes
    path('api/', include('blog_app.urls')),

    # ✅ THIS FIXES YOUR /blog/ ROUTE
    path('blog/', views.blog_list, name='blog_list'),

    # Optional: Redirect homepage to /blog/
    path('', RedirectView.as_view(url='/blog/', permanent=False)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
