from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ManutencaoF
from .models import Manutencao, Veiculo

#---------------------------------------------------------------------------------


@login_required
def manuadd(request):
    if request.method == 'POST':
        form = ManutencaoF(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.usuario = request.user
            manutencao.save()
            return redirect('manuListar')
    else:
        form = ManutencaoF()

    return render(request, 'manutencao/manuadd.html', {'form': form})

#---------------------------------------------------------------------------------

def manuListar(request):
    manutencao = Manutencao.objects.all()
    return render(request, 'manutencao/manuListar.html', {'manutencao': manutencao})

#---------------------------------------------------------------------------------

@login_required
def manuEditar(request, id):
    manutencao = get_object_or_404(Manutencao, id = id)
    if request.method == 'POST':
        manu = ManutencaoF(request.POST, instance= manutencao)
        if manu.is_valid():
            manu.save()
            return redirect('manuListar')
    else:
        manu = ManutencaoF(instance = manutencao)
    return render(request, 'manutencao/manuEditar.html', {'manutencao': manu})

#---------------------------------------------------------------------------------

@login_required
def manuDeletar(request, id):
        manutencao = get_object_or_404(Manutencao, pk=id, usuario=request.user)
        if request.method == 'POST':
            manutencao.delete()
            return redirect('manuListar')
        return render(request, 'manutencao/manuDeletar.html', {'manutencao': manutencao})

#---------------------------------------------------------------------------------

@login_required
def manuDetalhe(request, id):
    manutencao = get_object_or_404(Manutencao, id=id)
    return render(request, 'manutencao/manuDetalhe.html', {'manutencao': manutencao})

#---------------------------------------------------------------------------------
