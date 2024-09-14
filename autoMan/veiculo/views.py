from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Veiculo
from .forms import VeiculoF


#---------------------------------------------------------------------------------
@login_required
def veiculoAdd(request):

    if request.method == 'POST':
        veiculo = VeiculoF(request.POST)
        if veiculo.is_valid():
            veiculo.save()
            return redirect('veiculo')
    else:
        veiculo = VeiculoF()
    return render(request, 'veiculo/veiculo_add.html', {'veiculo': veiculo})

#---------------------------------------------------------------------------------

@login_required
def veiculoEditar(request, id):
    veiculo = get_object_or_404(Veiculo, pk = id)

    if request.method == 'POST':
        veicu = VeiculoF(request.POST, instace = veiculo)
        if veicu.is_valid():
            veicu.save()
            return redirect('veiculoLista')
    else:
        veicu = VeiculoF(instace = veiculo)
    return render(request, 'veiculo/veiculoEditar.html', {'veiculo': veiculo})

#---------------------------------------------------------------------------------

@login_required
def veiculoDeletar(request, id):
    veiculo = get_object_or_404(Veiculo, pk = id, usuario = request.user)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculoLista')
    return render(request, 'veiculo/veiculoDeletar.html', {'veiculo': veiculo})

#----------------------------------------------------------------------------------

def veiculoLista(request ):
    veicu = VeiculoF(request.get)
        
    return render(request, 'veiculo/veiculoListar.html', {'veiculo': veicu})

#----------------------------------------------------------------------------------

@login_required
def veiculoDetalhe(request, id):
    veicu = get_object_or_404(Veiculo, pk=id)
    return render(request,'veiculo/veiculoDetalhe.html', {'veiculo': veicu})

#----------------------------------------------------------------------------------