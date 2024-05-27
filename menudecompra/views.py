import json
import os

import logging


from django.shortcuts import render,redirect,get_object_or_404

#Django
from ProyectoWelcome.settings import MEDIA_ROOT
from menudecompra.models import Category,Product
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from django.contrib import messages

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def view_CategoriasComidas(request):
    categories = Category.objects.all()
    return render(request, 'categoria/categoriasComidas.html', {'categories': categories})


def view_menu_compra(request, category_id):

    category = get_object_or_404(Category, category_id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'menu_compra/menuCompra.html', {'category': category, 'products': products})


    
def finalizar_seleccion(request, category_id):
    if request.method == 'POST':
        # Aquí puedes manejar la lógica de los productos seleccionados
        # Por ejemplo, puedes obtener los productos seleccionados de la solicitud POST
        selected_products = request.POST.getlist('carrito')
        quantities = {key: value for key, value in request.POST.items() if key.startswith('quantity_')}
        # Haz algo con los productos seleccionados y sus cantidades
        # Por ejemplo, guardarlos en el carrito de compras del usuario

        return redirect('some_success_page')  # Redirige a una página de éxito o similar
    else:
        return redirect('menucompra', category_id=category_id)

#Funcion para añadir 

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm()
    return render(request, 'opcionesUsuario/add_product.html', {'form': form})
    

#vistas para editar producto

@login_required
def select_category_to_edit(request):
    categories = Category.objects.all()
    return render(request, 'opcionesUsuario/paso1edit.html', {'categories': categories})

@login_required
def select_product_to_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'opcionesUsuario/paso2edit.html', {'category': category, 'products': products})

#el que realiza el trabajo de editar:
logger = logging.getLogger(__name__)
"""
@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            try:
                # Eliminar la imagen anterior si se ha subido una nueva
                if 'photo' in request.FILES:
                    old_photo_path = product.photo.path
                    logger.debug(f"Old photo path: {old_photo_path}")
                    product.photo = request.FILES['photo']
                    product.save()

                    # Ahora elimina la foto antigua
                    if os.path.exists(old_photo_path):
                        os.remove(old_photo_path)
                        logger.debug(f"Old photo removed: {old_photo_path}")
                    else:
                        logger.debug(f"Old photo not found: {old_photo_path}")

                else:
                    form.save()

                messages.success(request, 'Producto actualizado correctamente.')
                return redirect('select_product_to_edit', category_id=product.category.category_id)
            except Exception as e:
                logger.error(f"Error saving product: {e}")
                messages.error(request, f'Error al actualizar el producto: {e}')
        else:
            logger.error("Form is not valid")
            logger.error(form.errors)
    else:
        form = ProductForm(instance=product)

    return render(request, 'opcionesUsuario/edit_product.html', {'form': form, 'product': product, 'category_id': product.category.category_id})
"""

#funcion para corroborar si se puede borrar las fotos
"""
@login_required
def test_delete_file(request):
    test_file_path = os.path.join(MEDIA_ROOT, 'product_images', 'cajaProducto_2viYmMs.jpg')  # Cambia 'nombre_de_la_imagen.jpg' por el nombre del archivo que deseas probar

    try:
        if os.path.exists(test_file_path):
            os.remove(test_file_path)
            return JsonResponse({'status': 'success', 'message': f'Archivo {test_file_path} eliminado correctamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': f'Archivo {test_file_path} no encontrado.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
"""
@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            try:
                old_photo_path = None
                if 'photo' in request.FILES:
                    if product.photo and hasattr(product.photo, 'path'):
                        old_photo_path = product.photo.path
                    product.photo = request.FILES['photo']
                form.save()

                if old_photo_path:
                    request.session['old_photo_path'] = old_photo_path

                messages.success(request, 'Producto actualizado correctamente.')
                return redirect('edit_product', product_id=product.id)
            except Exception as e:
                logger.error(f"Error saving product: {e}")
                messages.error(request, f'Error al actualizar el producto: {e}')
        else:
            logger.error("Form is not valid")
            logger.error(form.errors)
    else:
        form = ProductForm(instance=product)

    return render(request, 'opcionesUsuario/edit_product.html', {'form': form, 'product': product, 'category_id': product.category.category_id})

@login_required
@csrf_exempt
def delete_old_photo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            old_photo_path = data.get('old_photo_path')
            if old_photo_path and os.path.exists(old_photo_path):
                os.remove(old_photo_path)
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'error', 'message': 'La imagen no existe.'})
        except Exception as e:
            logger.error(f"Error al eliminar la imagen antigua: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})


@login_required
@csrf_exempt
def clear_old_photo_session(request):
    if request.method == 'POST':
        try:
            del request.session['old_photo_path']
        except KeyError:
            pass
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})



#eliminar producto entero

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        category_id = product.category.category_id
        product.delete()
        return redirect('select_product_to_edit', category_id=category_id)
    return render(request, 'opcionesUsuario/confirm_delete.html', {'product': product})