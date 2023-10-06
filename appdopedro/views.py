from django.shortcuts import render, redirect
from .models import Filmes, Jogos

def home(request):
  filmes = Filmes.objects.all()
  jogos = Jogos.objects.all()
  
  return render(request, "home.html", context={ 
    "flm": filmes,
    "jogos": jogos
  })

def create_filme(request):
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    Filmes.objects.create(
      titulo = request.POST["titulo"],
      diretor = request.POST["diretor"],
      genero = request.POST["genero"],
      lancamento = request.POST["lancamento"]
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

def update_filme(request, id):
  filme = Filmes.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    filme.titulo = request.POST["titulo"]
    filme.diretor = request.POST["diretor"]
    filme.genero = request.POST["genero"]
    filme.lancamento = request.POST["lancamento"]
    filme.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","filme": filme})

def delete_filme(request, id):
  filme = Filmes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      filme.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"filme": filme})