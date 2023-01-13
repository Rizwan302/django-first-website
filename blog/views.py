from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlockComment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost' : allpost}
    return render(request, 'blog/bloghome.html', context)


# it page blog content to smal reading blog 
def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()

    comment = BlockComment.objects.filter(post=post, parent=None)
    replies = BlockComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)


    context = {'post':post, 'comment':comment, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'blog/blogpost.html', context)

    # click your button blog full post reading
    
def postcomments(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        
        if parentSno == '':
            comment=BlockComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlockComment.objects.get(sno=parentSno)
            comment=BlockComment(comment= comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request, "Your Reply has been posted successfully") 

    
    return redirect(f"/blog/{post.slug}")

