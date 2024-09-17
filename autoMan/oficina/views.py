from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OficinaF
from .models import Oficina


#---------------------------------------------------------------------------------

@login_required
def oficinaAdd(request):
    if request.method == 'POST':
        ofi = OficinaF(request.POST, request.FILES)
        if ofi.is_valid():
            oficina = ofi.save(commit=False) 
            oficina.usuario = request.user 
            ofi.save()
            return redirect('oficinaListar')
    else:
        ofi = OficinaF()
    return render(request, 'oficina/oficinaAdd.html',{'ofi' : OficinaF})

#---------------------------------------------------------------------------------

@login_required
def oficinaListar(request):
    oficinas = Oficina.objects.all()  
    return render(request, 'oficina/oficinaListar.html', {'oficinas': oficinas})


#---------------------------------------------------------------------------------

@login_required
def oficinaEditar(request, id):
    ofi = get_object_or_404(Oficina, id = id)
    if request.method == 'POST':
        ofi = OficinaF(request.POST, request.FILES, instance = ofi)
        if ofi.is_valid():
            ofi.save()
            return redirect('oficinaListar')
    else:
        ofi = OficinaF(instance = ofi)
    return render(request, 'oficina/oficinaEditar.html', {'ofi' : ofi})

#---------------------------------------------------------------------------------

@login_required
def oficinaDeletar(request, id):
    ofi = get_object_or_404(Oficina, pk = id, usuario = request.user)
    if request.method == 'POST':
        ofi.delete()
        return redirect('oficinaListar')
    return render(request, 'oficina/oficinaDeletar.html', {'ofi' : ofi})

#---------------------------------------------------------------------------------

def oficinaDetalhe(request, id):
    oficina = get_object_or_404(Oficina, id=id)
    return render(request, 'oficina/oficinaDetalhe.html', {'oficina': oficina})

#---------------------------------------------------------------------------------