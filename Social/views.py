from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from Account.models import CustomUser
from .forms import PostCreationForm, CommentForm
from .models import Post, Comment, Photo, Video, Message, Share
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import redirect, reverse
from rest_framework import generics, permissions, status, viewsets
from .serializers import PostSerializer, CommentSerializer, MessageSerializer, ShareSerializer, PhotoSerializer, \
    VideoSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        slug = slugify(title)
        serializer.save(author=self.request.user, slug=slug)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = Comment.objects.filter(post=post)

#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.user = request.user
#             comment.save()

#     else:
#         form = CommentForm()

#     return render(request, 'social/post/detail.html', {'post': post, 'comments': comments, 'form': form})


# @login_required
# def create_post(request):
#     if not (request.user.is_teacher or request.user.is_student):
#         return HttpResponse("Unauthorized", status=401)
#     user = request.user
#     if request.method == 'POST':
#         form = PostCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)

#             # Assign the user to the post author
#             post.author = user
#             # Handle Video creation
#             video_file = form.cleaned_data.get("video_file")
#             if video_file:
#                 video = Video.objects.create(video_file=video_file)
#                 post.video = video
#             # Handle Photo creation

#             if not post.slug:
#                 post.slug = slugify(post.title)

#             post.save()
#             image_files = request.FILES.getlist("image_files")
#             if image_files:
#                 for image_file in image_files:
#                     photo = Photo.objects.create(image=image_file)
#                     post.photos.add(photo)
#             return redirect('social:post_detail', pk=post.pk)


#     else:
#         form = PostCreationForm(user=request.user)

#     return render(request, 'social/post/create.html', {'form': form, 'user': user})


# @login_required
# def send_message(request, recipient_id):
#     has_message = Message.objects.filter(
#         Q(sender=request.user, recipient_id=recipient_id) |
#         Q(sender_id=recipient_id, recipient=request.user)
#     ).exists()

#     if has_message:
#         return redirect(reverse('social:conversation', args=[recipient_id]))

#     if request.method == 'POST':
#         content = request.POST['content']
#         recipient = CustomUser.objects.get(pk=recipient_id)
#         message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
#         return redirect(reverse('social:conversation', args=[recipient_id]))
#     if request.user == CustomUser.objects.get(pk=recipient_id):
#         return HttpResponse('Fobidden')

#     return render(request, 'social/send_message.html')


# @login_required
# def inbox(request):
#     conversations = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).values('sender',
#                                                                                                       'recipient').annotate(
#         latest_message=Max('timestamp'))

#     conversation_dict = {}

#     for conversation in conversations:
#         if conversation['sender'] == request.user.pk:
#             other_user_id = conversation['recipient']
#         else:
#             other_user_id = conversation['sender']

#         if other_user_id not in conversation_dict:
#             conversation_dict[other_user_id] = {
#                 'other_user': CustomUser.objects.get(pk=other_user_id),
#                 'latest_message': None
#             }

#         latest_message = Message.objects.filter(
#             Q(sender=conversation['sender'], recipient=request.user) | Q(sender=request.user,
#                                                                          recipient=conversation['sender'])
#         ).order_by('-timestamp').first()

#         if latest_message:
#             conversation_dict[other_user_id]['latest_message'] = latest_message

#     conversations = sorted(list(conversation_dict.values()),
#                            key=lambda conv: (conv['latest_message'].timestamp if conv['latest_message'] else None),
#                            reverse=True)

#     return render(request, 'social/inbox.html', {'conversations': conversations})


# @login_required
# def conversation(request, other_user_id):
#     other_user = get_object_or_404(CustomUser, pk=other_user_id)
#     messages = Message.objects.filter(
#         Q(sender=request.user, recipient=other_user) | Q(sender=other_user, recipient=request.user)
#     ).order_by('timestamp')

#     if request.method == 'POST':
#         content = request.POST.get('content')
#         recipient_id = request.POST.get('recipient_id')
#         recipient = get_object_or_404(CustomUser, pk=recipient_id)
#         message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
#         return redirect(reverse('social:conversation', args=[other_user_id]))

#     return render(request, 'social/conversation.html', {'messages': messages, 'other_user': other_user})


# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#     return redirect('social:post_detail', pk=pk)


# def share_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     share = Share.objects.create(post=post, shared_by=request.user)
#     return render(request, 'social/post/detail.html', {'post': post, 'share': share})
