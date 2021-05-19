from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')

def new_show(request):
    return render(request, "newShow.html")

def create(request):
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
    
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            desc = request.POST['description'],
            release_date = request.POST['rls_date']
        )
        messages.success(request, 'Show agregado exitosamente')
        idShow = Show.objects.last().id
        return redirect(f'/shows/{idShow}')

def show(request, idShow):
    show = Show.objects.get(id = int(idShow))
    context = {
        'show': show
    }
    return render(request, 'show.html', context)

def displayShows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'displayShows.html', context)

def edit(request, idShow):
    show = Show.objects.get(id = int(idShow))
    context = {
        'show': show
    }
    return render(request, 'editShow.html', context)

def update(request, idShow):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{idShow}/edit')
        #return render(request, 'editShow.html')
        '''
        errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:'''
    else:
        show_to_update = Show.objects.get(id=int(idShow))
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.desc = request.POST['description']
        show_to_update.release_date = request.POST['rls_date']
        show_to_update.save()
        messages.success(request, "Show actualizado correctamente")
        return redirect(f'/shows/{idShow}')

def destroy(request, idShow):
    show_to_delete = Show.objects.get(id=int(idShow))
    show_to_delete.delete()
    return redirect('/shows')