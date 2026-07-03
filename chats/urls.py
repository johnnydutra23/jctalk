from django.urls import path

from chats.views.chats import ChatsView, ChatView

from chats.views.massages import ChatMessagesView, ChatMessageView 

urlpatterns = [
    path('', ChatsView.as_view()),
    path('<int:chat_id>/', ChatView.as_view()),
    path('<int:chat_id>/messages/', ChatMessagesView.as_view()),
    path('<int:chat_id>/messages/<int:message_id>/', ChatMessageView.as_view()),
]

