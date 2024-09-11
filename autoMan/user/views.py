from django.shortcuts import render
 
from user.models import User
from django.contrib.auth.models import User 
# Create your views here.


#---------------------------------------------------------------------------------
@login_required
def addUser(request):
    if resquest.method == 'POST':
        USERFORM = UserForm(request.POST)
        USUARIO = usuario(request.POST, request.FILES)

        #validando user

        if USUARIO.is_valid() and USUARIOS.is_valid():
            user = USERFORM.save(commit=False)
            user.set_password(USUARIO.cleaned_data['password'])
            user.save()

        #validado usuario 

        usuario = USUARIO.save(commit=False)
        usuario.user = user
        usuario.save()

        login(request, user)
        return redirect('home')

    else:
        USERFORM = UserForm()
        USUARIO = UserForm()    
    
    return render(request, 'addUser.html', {'USUARIO': USUARIO, 'USERFORM': USERFORM})


    #---------------------------------------------------------------------------------


@login_required
def editar(request, usuario_id):

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
        raise permissionDenied 