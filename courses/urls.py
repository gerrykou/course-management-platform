from django.urls import path
from . import views


urlpatterns = [
    path("", views.course_list, name="course_list"),
    path(
        "<slug:course_slug>/",
        views.course_detail,
        name="course_detail",
    ),
    path(
        "<slug:course_slug>/leaderboard",
        views.leaderboard_view,
        name="leaderboard",
    ),
    path(
        "<slug:course_slug>/leaderboard/<int:enrollment_id>/",
        views.leaderboard_detail,
        name="leaderboard_detail",
    ),
    path(
        "<slug:course_slug>/enrollment",
        views.enrollment_detail,
        name="enrollment_detail",
    ),
    path(
        "<slug:course_slug>/project/<slug:project_slug>",
        views.project_view,
        name="project_view",
    ),
    path(
        "<slug:course_slug>/homework/<slug:homework_slug>",
        views.homework_detail,
        name="homework_detail",
    ),

]
