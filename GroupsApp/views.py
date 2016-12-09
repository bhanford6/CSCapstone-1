"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project
from UsersApp.models import Student
from UsersApp.models import Engineer
from CompaniesApp.models import Company
from CommentsApp.models import Comment
from CommentsApp.forms import CommentForm
from operator import itemgetter
import cgi
import datetime
import re

def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        members = in_group.members.all()
        user = request.user
        print in_group.project
        try:
            project = in_group.project
        except:
            project = None
 
        context = {
            'group' : in_group,
            'userIsMember': is_member,
            'user'  : user,
            'project' : project,
            'members' : members,
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupForm(request):
    if request.user.is_authenticated():
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                new_group.save()
                new_group.members.add(request.user)
                new_group.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.add(request.user)
        in_group.save();
        request.user.group_set.add(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': True,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')
    
def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.remove(request.user)
        in_group.save();
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': False,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def projectsGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        projects = Project.objects.all()
        members = in_group.members.all()
        context = {
            'group'     : in_group,
            'projects'  : projects,
            'members'   : members,
        }
        return render(request, 'projectsgroup.html', context)
        
    return render(request, 'autherror.html')

def membersGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        members = in_group.members.all()
        try:
            is_member = members.get(id__exact=request.user.id)
        except:
            is_member = False
        context = {
            'group'     : in_group,
            'members'   : members,
            'is_member' : is_member,
        }
        return render(request, 'membersgroup.html', context)
    return render(request, 'autherror.html')

def addMembers(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        users = MyUser.objects.all()
        context = {
            'group'     : in_group,
            'users'     : users
        }
        return render(request, 'addmembers.html', context)
    return render(request, 'autherror.html')

def addMember(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        memberid = request.GET.get('id', 'None')
        member = MyUser.objects.get(id__exact=memberid)
        in_group.members.add(member)
        in_group.save()
        context = {
            'group'     : in_group,
            'member'    : member,
        }
        return render(request, 'addmember.html', context)
    return render(request, 'autherror.html')

def remove(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.delete()
        context = {
            'group' : in_group,
        }
        return render(request, 'removegroup.html', context)
    return render(request, 'autherror.html')

def assignGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        user = request.user
        comp = None
        projects = None

        # check that the engineer is apart of an existing company
        try:
            eng = Engineer.objects.get(ident__exact=user.id)
            comp = Company.objects.get(name__exact=eng.company)
        except:
            comp = None 

        if comp != None:
            try:
                projects = comp.projects.all()
            except:
                projects = None

        context = {
            'group'     : in_group,
            'user'      : user,
            'company'   : comp,
            'engineer'  : eng,
            'projects'   : projects,
        }
        return render(request, 'assigngroup.html', context)
    return render(reqeust, 'autherror.html')

def assignedGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        user = request.user
        in_project = request.GET.get('project','None')
        project = models.Project.objects.get(name__exact=in_project)
        in_group.project = project
        in_group.save()
        context = {
            'group'     : in_group,
            'user'      : user,
            'project'   : project,
        }
        return render(request, 'assignedgroup.html', context)
    return render(request, 'autherror.html')

def recProject(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        user = request.user
        project_list = Project.objects.all()
        member_user_list = in_group.members.all()
        member_list = []
        group_list = []
        group_attr = [] 
        project_attrs_list = []
        project_rank = [] 

        # list of each project's attributes list
        for project in project_list:
            project_attrs_list.append(re.split(r'<.*?>|\s+', project.knowledge))

        # creating list of Students to access 
        # student attributes
        for member_user in member_user_list:
            if member_user.is_admin:
                continue;
            if member_user.is_student:
                member_list.append(Student.objects.get(ident__exact=member_user.id))

        # combining all student attributes into a 
        # single list of 'group attributes'
        for member in member_list:
            group_attr = []
            group_attr.extend(re.split(r'<.*?>|\s+', member.skills)) #or r'&.*?;', member.skills))
            #group_attr.extend(re.split(r'&.*?;', group_a
            i = 0
            for skill in group_attr:
                group_attr[i] = re.sub(r'&.*?;', '',skill).strip()
                i+=1
                if len(skill) < 1:
                    continue
            group_attr = [re.sub(r'&.*?', '', x) if len(re.sub(r'&.*?;', '', x).strip()) > 0 else None for x in group_attr]
            group_list.append(group_attr)
        for project_attrs in project_attrs_list:
            rank = 0
            for group_attr in group_list:
                for attr in project_attrs:
                    attr = re.sub(r'&.*?;|\r\n|\n', '', attr)
                    attr.strip()
                    if len(attr) < 1:
                        continue
                    if attr in group_attr:
                        rank += 1
             
            project_rank.append(rank)
        proj_rank_zipped = zip(project_list, project_rank)
        proj_rank_zipped = filter(lambda x: x[1] > 0, proj_rank_zipped)
        proj_rank_sorted = sorted(proj_rank_zipped, key=itemgetter(1), reverse=True)
        print proj_rank_zipped
        context = {
            'projRanks'     : proj_rank_sorted,
            'group'         : in_group,
            'user'          : user,
        }
        return render(request, 'projrecs.html', context) 
    return render(request, 'autherror.html')

def requestJoin(request):
    if request.user.is_authenticated():
        in_group = request.GET.get('name', 'None')
        group = models.Group.objects.get(name__exact=in_group)
        user = request.user
        requesting = user.get_full_name() + " has requested to join the group."
        reqComment = Comment(time=datetime.datetime.now(), group_name=in_group, comment=requesting)
        reqComment.save()
        print reqComment.comment
        group.save()
        print len(group.comments.all())
        group.comments.add(reqComment)
        group.save()
        print len(group.comments.all())
        context = {
            'group' : group,
            'user'  : user,
        }
        return render(request, 'requestjoin.html', context)
    return render(request, 'autherror.html')

def groupComments(request):
    if request.user.is_authenticated():
        in_group = request.GET.get('name', 'None')
        group = models.Group.objects.get(name__exact=in_group)
        user = request.user
        comments = group.comments.filter(group_name__exact=in_group)
        context = {
            'group'     : group,
            'user'      : user,
            'comments'  : comments,
        }
        return render(request, 'groupcomments.html', context)
    return render(request, 'autherror.html')

def groupCommentForm(request):
    in_group = request.GET.get('name', 'None')
    group = models.Group.objects.get(name__exact=in_group)
    context = {
        'group' : group
    }
    return render(request, 'groupcommentform.html', context)

def groupAddComment(request):
    if request.user.is_authenticated():
        in_group = request.GET.get('name', 'None')
        group = models.Group.objects.get(name__exact=in_group)
        user = request.user
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = Comment(comment=form.cleaned_data['comment'])
                new_comment.group_name = in_group
                new_comment.save()
                print len(group.comments.all())
                group.comments.add(new_comment)
                group.save()
                print len(group.comments.all())
                context = {
                    'group'     : group,
                    'comments'  : group.comments.all(),
                    'user'      : user,
                }
                return render(request, 'groupcomments.html', context)
    return render(request, 'autherror.html')

