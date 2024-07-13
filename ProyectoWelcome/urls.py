"""
URL configuration for ProyectoWelcome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ProyectoWelcome import views as local_views
from inicio import views as inicio_views
from users import views as users_views
from menudecompra import views as compra_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('inicio/',local_views.hello_word),
    path('hi/<str:name>/<int:age>',local_views.say_hi),#es una vista que va a recibir dos argumentos
    #ya indico los nombres de los argumentos
    path('',inicio_views.viewIndex,name="inicio"),
    
    path('users/login/',users_views.login_view,name="login"),
    path('users/logout/',users_views.logout_view,name="logout"),
    
    path('categorias/',compra_views.view_CategoriasComidas,name='categorias'),
    path('menucompra/<int:category_id>/',compra_views.view_menu_compra, name='menucompra'),

    path('finalizar_seleccion/<int:category_id>/', compra_views.finalizar_seleccion, name='finalizar_seleccion'),

        #path para añadir producto
    path('add_product/',compra_views.add_product, name='add_product'),

    #path para editar
    #path('edit_product/<int:product_id>/', compra_views.edit_product, name='edit_product'),



    #editar producto


    path('editar-categoria/', compra_views.select_category_to_edit, name='select_category_to_edit'),
    path('editar-productos/<int:category_id>/',compra_views.select_product_to_edit, name='select_product_to_edit'),
    path('editar-producto/<int:product_id>/', compra_views.edit_product, name='edit_product'),
    path('eliminar-producto/<int:product_id>/', compra_views.delete_product, name='delete_product'),

    #eliminar foto cuando se edita un producto
    #path('delete_old_photo/', compra_views.delete_old_photo, name='delete_old_photo'),
    #path('clear_old_photo_session/', compra_views.clear_old_photo_session, name='clear_old_photo_session'),

    #path('test-delete-file/', compra_views.test_delete_file, name='test_delete_file'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
