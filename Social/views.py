from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from Account.models import CustomUser
from .forms import PostCreationForm
from .models import Post, Comment, Photo, Video, Message
from django.shortcuts import get_object_or_404


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'social/post/detail.html', {'post': post})


@login_required
def create_post(request):
    if not (request.user.is_teacher or request.user.is_student):
        return HttpResponse("Unauthorized", status=401)
    user = request.user
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # Assign the user to the post author
            post.author = user
            # Handle Video creation
            video_file = form.cleaned_data.get("video_file")
            if video_file:
                video = Video.objects.create(video_file=video_file)
                post.video = video
            # Handle Photo creation

            if not post.slug:
                post.slug = slugify(post.title)

            post.save()
            image_files = request.FILES.getlist("image_files")
            if image_files:
                for image_file in image_files:
                    photo = Photo.objects.create(image=image_file)
                    post.photos.add(photo)
            return redirect('social:post_detail', pk=post.pk)


    else:
        form = PostCreationForm(user=request.user)

    return render(request, 'social/post/create.html', {'form': form, 'user': user})


def chat_view(request):
    return render(request, 'social/chat.html')


@login_required
def send_message(request, recipient_id):
    if request.method == 'POST':
        content = request.POST['content']
        recipient = CustomUser.objects.get(pk=recipient_id)
        message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
        return redirect('social:message_sent')
    return render(request, 'social/send_message.html')


@login_required
def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    messages = received_messages | sent_messages
    return render(request, 'social/inbox.html', {'messages': messages, 'user': request.user})



def message_sent(request):
    return render(request, 'social/message_sent.html')