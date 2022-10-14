from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from familiar.models import Familiar

def create_familiar(request, name: str, birth_date: str, fav_number: int):

    template = loader.get_template("template_familiar.html")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    familiar = Familiar(name=name, birth_date=birth_date, fav_number=fav_number)
    familiar.save()  # save into the DB

    context_dict = {"familiar": familiar}
    render = template.render(context_dict)
    return HttpResponse(render)

def familiars(request):
    familiars = Familiar.objects.all()

    context_dict = {"familiars": familiars}

    return render(
        request=request,
        context=context_dict,
        template_name="familiar/familiar_list.html",
    )