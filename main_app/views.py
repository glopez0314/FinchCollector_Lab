from django.shortcuts import render, redirect
from .models import Dog, Trick
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import PlaydateForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, "dogs/index.html", {"dogs": dogs})


def dogs_details(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    id_list = dog.tricks.all().values_list("id")
    tricks_dog_doesnt_know = Trick.objects.exclude(id__in=id_list)
    playdate_form = PlaydateForm()
    return render(
        request,
        "dogs/details.html",
        {"dog": dog, "playdate_form": playdate_form, "tricks": tricks_dog_doesnt_know},
    )


class DogCreate(CreateView):
    model = Dog
    fields = "__all__"


class DogUpdate(UpdateView):
    model = Dog
    fields = ["age", "behavior"]


class DogDelete(DeleteView):
    model = Dog
    success_url = "/dogs"


def add_playdate(request, dog_id):
    form = PlaydateForm(request.POST)
    if form.is_valid():
        new_playdate = form.save(commit=False)
        new_playdate.dog_id = dog_id
        new_playdate.save()
    return redirect("details", dog_id=dog_id)


class TrickList(ListView):
    model = Trick


class TrickDetail(DetailView):
    model = Trick


class TrickCreate(CreateView):
    model = Trick
    fields = "__all__"


class TrickUpdate(UpdateView):
    model = Trick
    fields = "__all__"


class TrickDelete(DeleteView):
    model = Trick
    success_url = "/tricks"


def assoc_trick(request, dog_id, trick_id):
    Dog.objects.get(id=dog_id).tricks.add(trick_id)
    return redirect("details", dog_id=dog_id)


def unassoc_trick(request, dog_id, trick_id):
    Dog.objects.get(id=dog_id).tricks.remove(trick_id)
    return redirect("details", dog_id=dog_id)
