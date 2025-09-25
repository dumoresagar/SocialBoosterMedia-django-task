from django.core.management.base import BaseCommand
from items.models import ExternalPost
import requests

class Command(BaseCommand):
    help = "Import posts from JSONPlaceholder"

    def handle(self, *args, **options):
        url = "https://jsonplaceholder.typicode.com/posts"
        resp = requests.get(url)
        if resp.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch"))
            return
        data = resp.json()
        created = 0
        for p in data:
            obj, was_created = ExternalPost.objects.get_or_create(
                external_id=p["id"],
                defaults={"title": p["title"], "body": p["body"]},
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Imported: {created} posts."))
