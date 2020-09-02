from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    """Main site for Learning Log app"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Display single topic and all of its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data, create blank form
        form = TopicForm()
    else:
        # Got POST data, need to be processed
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Displaying blank form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add new entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data, create blank form
        form = EntryForm()
    else:
        # Got POST data, need to be processed
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Displaying blank form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
