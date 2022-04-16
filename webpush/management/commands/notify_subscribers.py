from django.core.management.base import BaseCommand
from webpush.models import WebPushNotificationUsers
from webpush.views import send_notification
from users.models import Post
from django.conf import settings
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
class Command(BaseCommand):
    # define logic of command
    def handle(self, *args, **options):
        posts = Post.objects.all()[:2]
        for post, link in zip(posts, ALLOWED_HOSTS):
            resgistration = []
            qs = WebPushNotificationUsers.objects.all()
            for device in qs:
                resgistration.append(device.registration_id)
            send_notification(resgistration, post.title, post.description, post.image_url, message_link=f"//{link}/{post.id}")
        self.stdout.write( 'Notification Was Done Sucessfully ✅' )