from django.urls import path

# Tambahkan get_projects_json di sini
from main.views import (
    show_experience, 
    show_main, 
    show_skills, 
    create_project, 
    show_projects,
    get_projects_json,
    delete_project,
    show_experience_json,
    add_experience,
    edit_experience,
    delete_experience,
    register,
    login_user,
    logout_user,
    toggle_star,
    edit_project
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("experience/json/", show_experience_json, name="show_experience_json"),
    path("experience/add/", add_experience, name="add_experience"),
    path("experience/edit/<uuid:id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<uuid:id>/", delete_experience, name="delete_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/<uuid:project_id>/edit/", edit_project, name="edit_project"),
]