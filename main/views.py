from django.shortcuts import render

from main.models import Experience, Skill


def show_main(request):
    context = {
        "name": "Piedra Ridwan Azra Pulungan",
        "npm": "2506623055",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Piedra Ridwan Azra Pulungan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_skills(request):
    context = {
        "name": "Piedra Ridwan Azra Pulungan",
        "skills_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)