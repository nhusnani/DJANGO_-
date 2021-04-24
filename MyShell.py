import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()

for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")

for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
print()

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)