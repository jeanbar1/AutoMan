from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Veiculo
from .forms import VeiculoF


#---------------------------------------------------------------------------------
@login_required
def veiculoAdd(request):
    if request.method == 'POST':
        form = VeiculoF(request.user, request.POST)
        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.usuario = request.user  
            veiculo.save()
            return redirect('veiculoListar')
    else:
        form = VeiculoF(request.user)
    
    return render(request, 'veiculo/veiculoadd.html', {'form': form})

#---------------------------------------------------------------------------------

@login_required
def veiculoEditar(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    
    if request.method == 'POST':
        form = VeiculoF(user=request.user, data=request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculoListar')
    else:
        form = VeiculoF(user=request.user, instance=veiculo)

    return render(request, 'veiculo/veiculoEditar.html', {'veiculos_form': form})


#---------------------------------------------------------------------------------

@login_required
def veiculoDeletar(request, id):
    veiculo = get_object_or_404(Veiculo, id = id, proprietario = request.user)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculoListar')
    return render(request, 'veiculo/veiculoDeletar.html', {'veiculo': veiculo})

#----------------------------------------------------------------------------------
@login_required
def veiculoListar(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculo/veiculoListar.html', {'veiculos': veiculos})


#----------------------------------------------------------------------------------

@login_required
def veiculoDetalhe(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'veiculo/veiculoDetalhe.html', {'veiculo': veiculo})

#----------------------------------------------------------------------------------