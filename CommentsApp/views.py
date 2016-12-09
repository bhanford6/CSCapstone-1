from django.shortcuts import render

from . import models
from . import forms
def getComments(request):
    comments_list = models.Comment.objects.filter(group_name__exact=None)
    for comment in comments_list:
        print comment.group_name

    context = {
        'comments' : comments_list
    }
    return render(request, 'comments.html', context)

def getCommentForm(request):
    return render(request, 'commentForm.html')

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
            comments_list = models.Comment.objects.filter(group_name__exact=None)
            context = {
                'comments' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')

def removeComment(request):
    if request.user.is_authenticated():
        in_id = request.GET.get('id', 'None')
        comment = models.Comment.objects.get(id__exact=in_id)
        comment.delete()
        return render(request, 'commentremoved.html')
    return render(reqeust, 'autherror.html')





