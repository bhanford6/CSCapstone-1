"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
	url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^group/projects$', views.projectsGroup, name='GProjects'),
    url(r'^group/members$', views.membersGroup, name='GMembers'),
    url(r'^group/members/add$', views.addMembers, name='AddMembers'),
    url(r'^group/member/add$', views.addMember, name='AddMember'),
    url(r'^group/remove$', views.remove, name='Remove'),
    url(r'^group/assign$', views.assignGroup, name='AssignGroup'),
    url(r'^group/assigned$', views.assignedGroup, name='AssignedGroup'),
    url(r'^group/projects/recommended$', views.recProject, name='RecommendedProjects'),
    url(r'^group/request$', views.requestJoin, name='RequestJoin'),
    url(r'^group/comments$', views.groupComments, name='GroupComments'),
    url(r'^group/comment/form$', views.groupCommentForm, name='GroupCommentForm'),
    url(r'^group/addcomment$', views.groupAddComment, name='GroupAddComment'),
]
