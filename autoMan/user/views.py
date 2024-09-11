from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from .forms import UserLogin, addUser, Usuario
from user.models import User
from django.contrib.auth.models import User 
# Create your views here.


#---------------------------------------------------------------------------------
@login_required
def addUser(request):
    if request.method == 'POST':
        USERFORM = user(request.POST)
        USUARIO = usuario(request.POST, request.FILES)

        #validando user

        if USUARIO.is_valid() and USUARIO.is_valid():
            user = USERFORM.save(commit=False)
            user.set_password(USUARIO.cleaned_data['password'])
            user.save()

        #validado usuario 

        usuario = USUARIO.save(commit=False)
        usuario.user = user
        usuario.save()

        login(request, user)
        return redirect('login')

    else:
        USERFORM = UserLogin()
        USUARIO = Usuario()    
    
    return render(request, 'addUser.html', {'USUARIO': USUARIO, 'USERFORM': USERFORM})


    #---------------------------------------------------------------------------------


@login_required
def editar(request, usuario_id):
    usuario = get_object_or_404(usuario, pk=usuario_id)

    if request.user.is_staff or request.user == usuario.user:
        if request.method == 'POST':
            edt = usuario(request.POST, request.FILES, instance=usuario)

            if edt.is_valid():
                edt.save()
                return redirect('home', {'usuario':'usuario'})
        else:
            edt = usuario(instance=usuario)
        return redirect('editar', {'edt': edt, 'usuario': usuario})
    else:
        raise PermissionDenied 
    
#---------------------------------------------------------------------------------


@login_required
def perfil(request):
    usuario = get_object_or_404(Usuario, pk=request.user)
    
    return render(request, 'perfil.html', {'usuario': usuario})

#---------------------------------------------------------------------------------

@login_required
def excluirP(request):
    if request.method == 'POST':
        User = get_object_or_404(User, pk=id)

        try: 
            usuario = Usuario.objects.get(user=User)
            Usuario.delete()
        except Usuario.DoesNotExist:
            pass
        
        User.delete()

        return redirect('login')
    else:
        return render(request, 'user/excluirP.html', {'user': get_object_or_404(User, pk=id)})

#---------------------------------------------------------------------------------

def login(request):
    if request.method == 'POST':
        login = UserLogin(data = request.POST)

        if login.is_valid():
            user = login.get_user()
            login(request, user)

            return redirect('home')
    else:
        login = UserLogin()

    return render(request, 'login/login.html', {'login': login})

#---------------------------------------------------------------------------------

def logout(request):
    logout(request)
    return redirect('login')

#---------------------------------------------------------------------------------