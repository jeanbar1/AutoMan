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
            ofi.save()
            return redirect('oficina')
    else:
        ofi = OficinaF()
    return render(request, 'oficina/oficinaAdd.html',{'ofi' : OficinaF})

#---------------------------------------------------------------------------------

@login_required
def oficinaListar(request):
    oficinas =  get_object_or_404(Oficina)
    return render(request, 'oficina/oficinaListar.html', {'oficinas' : oficinas})

#---------------------------------------------------------------------------------

@login_required
def oficinaEditar(request):
    ofi = get_object_or_404(Oficina, pk = id)
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