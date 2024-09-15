from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import UserLogin, addUser, UsuarioForm
from django.contrib.auth.models import User


#----------------------------------------------------------------
@login_required
def useradd(request):
    if request.method == 'POST':
        USERFORM = addUser(request.POST)
        USUARIO = UsuarioForm(request.POST, request.FILES)

        if USERFORM.is_valid() and USUARIO.is_valid():
            user = USERFORM.save(commit=False)
            user.set_password(USERFORM.cleaned_data['password'])
            user.save()

            usuario = USUARIO.save(commit=False)
            usuario.user = user
            usuario.save()

            auth_login(request, user)
            return redirect('home')

    else:
        USERFORM = addUser()
        USUARIO = UsuarioForm()

    return render(request, 'addUser.html', {'USUARIO': USUARIO, 'USERFORM': USERFORM})


#----------------------------------------------------------------

@login_required
def editar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if request.user.is_staff or request.user == usuario.user:
        if request.method == 'POST':
            edt = UsuarioForm(request.POST, request.FILES, instance=usuario)

            if edt.is_valid():
                edt.save()
                return redirect('home')
        else:
            edt = UsuarioForm(instance=usuario)
        return render(request, 'editar.html', {'edt': edt, 'usuario': usuario})
    else:
        raise PermissionDenied


@login_required
def perfil(request):
    usuario = get_object_or_404(Usuario, pk=request.user.id)
    
    return render(request, 'perfil.html', {'usuario': usuario})


#----------------------------------------------------------------

@login_required
def excluirP(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)

        try: 
            usuario = Usuario.objects.get(user=user)
            usuario.delete()
        except Usuario.DoesNotExist:
            pass
        
        user.delete()

        return redirect('login')
    else:
        return render(request, 'user/excluirP.html', {'user': get_object_or_404(User, pk=request.user.id)})



#----------------------------------------------------------------


def user_login(request):
    if request.method == 'POST':
        login_form = UserLogin(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)

            return redirect('home')
    else:
        login_form = UserLogin()

    return render(request, 'login/login.html', {'login': login_form})


#----------------------------------------------------------------


def user_logout(request):
    auth_logout(request)
    return redirect('login')
