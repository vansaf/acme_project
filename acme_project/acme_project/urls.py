from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path, reverse_lazy
from users.forms import CustomUserCreationForm

from django.conf import settings

handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('', include('pages.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('auth/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)