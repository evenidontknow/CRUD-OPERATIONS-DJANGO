from django.http import HttpResponse, HttpResponseNotFound
from .models import Notes
from .models import Items
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def home(request):
   if request.method == 'GET':    
       notes = Notes.objects.filter(user=request.user)
       items = Items.objects.all()
       return render(request,
           'notes.html',
           {'Notes':notes,'Items':items})
   elif request.method == 'POST': 
       try:
           Notes.objects.create(name=request.POST['note_name'],
                               user=request.user)
       except:
           return HttpResponse("Note already exists!")
       else:
           notes = Notes.objects.filter(user=request.user)
           items = Items.objects.all()
           return render(request,
               'notes.html',
               {'Notes':notes,'Items':items})    

@login_required(login_url='/login/')
def notes_view(request, id):
   try:
       note = Notes.objects.get(id=id, user=request.user)
   except:
       return HttpResponseNotFound("Not Found")
   else:
       if request.method=='GET':
           items=Items.objects.filter(note_id=note)
           return render(request,'items.html',
               {'Note':note,'Items':items})
       else:
           item_name=request.POST['item_name']
           Items.objects.create(item_name=item_name,note_id=note)
           items=Items.objects.filter(note_id=note)
           return render(request,'items.html',
               {'Note':note,'Items':items})
from .forms import NotesForm
@login_required(login_url='/login/')
def update_note(request, id):
  try:
      note = Notes.objects.get(id=id, user=request.user)
  except:
      return HttpResponseNotFound("Not Found")
  else:
      if request.method=='GET':
          form = NotesForm(instance=note)
          return render(request,'update_note.html',{'form':form})
      else:
          note.name=request.POST['name']
          note.save()
          return redirect('notes')
@login_required(login_url='/login/')
def delete_note(request, id):
  try:
      note = Notes.objects.get(id=id, user=request.user)
  except:
      return HttpResponseNotFound("Not Found")
  else:
      note.delete()
      return redirect('notes')

