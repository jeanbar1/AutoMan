from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ManutencaoF
from .models import Manutencao, Oficina, User

#---------------------------------------------------------------------------------

@login_required
def oficinaAdd(request):
    if request.method == 'POST':
        manu = ManutencaoF(request.POST)
        if manu.is_valid():
            manutencao = manu.save(commit = False)
            manutencao.usuario = request.user
            manutencao.save()
            return redirect('home')
    else:
        manu = ManutencaoF()
    return render(request, 'manutencao/oficinaAdd.html', {'manutencao': manu})

#---------------------------------------------------------------------------------

@login_required
def oficinaListar(request):
    usuario = request.user
    manutencao = Manutencao.objects.filter(usuario = usuario)
    return render(request, 'manutencao/oficinaListar.html', {'manutencao': manutencao})

#---------------------------------------------------------------------------------

@login_required
def oficinaEditar(request, id):
    manutencao = get_object_or_404(Manutencao, pk = id)
    if request.method == 'POST':
        manu = ManutencaoF(request.POST, instance= manutencao)
        if manu.is_valid():
            manu.save()
            return redirect('home')
    else:
        manu = ManutencaoF(instance = manutencao)
    return render(request, 'manutencao/oficinaEditar.html', {'manutencao': manu})

#---------------------------------------------------------------------------------

@login_required
def oficinaDeletar(request, id):
        manutencao = get_object_or_404(Manutencao, pk=id, usuario=request.user)
        if request.method == 'POST':
            manutencao.delete()
            return redirect('home')
        return render(request, 'manutencao/oficinaDeletar.html', {'manutencao': manutencao})

#---------------------------------------------------------------------------------