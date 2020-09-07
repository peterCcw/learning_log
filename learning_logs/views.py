from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Main site for Learning Log app"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Display all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id, message=None):
    """Display single topic and all of its entries"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'message': message}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data, create blank form
        form = TopicForm()
    else:
        # Got POST data, need to be processed
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            messages.success(request, f'Dodano temat: "{new_topic}"')
            return redirect('learning_logs:topics')

    # Displaying blank form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add new entry"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

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

            messages.success(request, f'Dodano wpis: "{new_entry}"')
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Displaying blank form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Initial request, fill form with current data
        form = EntryForm(instance=entry)
    else:
        # Got POST data, need to be processed
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Edytowano wpis: "{entry}" z dnia '
                                      f'{entry.date_added}')
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404

@login_required
def delete_entry(request, entry_id):
    """Delete specific entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != "POST":
        context = {'entry': entry}
        return render(request, 'learning_logs/delete_entry.html', context)
    else:
        entry.delete()
        messages.success(request, f'Usunięto wpis: "{entry}" z dnia '
                                  f'{entry.date_added}')
        return redirect('learning_logs:topic', topic_id=topic.id)

@login_required
def delete_topic(request, topic_id):
    """Delete specific topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    if request.method != "POST":
        context = {'topic': topic}
        return render(request, 'learning_logs/delete_topic.html', context)
    else:
        topic.delete()
        messages.success(request, f'Usunięto temat: "{topic}"')
        return redirect('learning_logs:topics')

@login_required
def edit_topic(request, topic_id):
    """Edit specific topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Initial request, fill form with current data
        form = TopicForm(instance=topic)
    else:
        # Got POST data, need to be processed
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dokonano edycji tematu: "{topic}"')
            return redirect('learning_logs:topics')
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)
