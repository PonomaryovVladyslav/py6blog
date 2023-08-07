from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _


class Seasion10mAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        # token = model.objects.select_related('user').get(key=key)
        # if (timezone.now() - token.created).seconds > (60 *10):
        #     raise exceptions.AuthenticationFailed("Sorry, 10 minutes have gone")
        try:
            token = model.objects.select_related('user').get(key=key)
            if (timezone.now() - token.created).seconds > (60* 10):
                raise exceptions.AuthenticationFailed("Sorry, 10 minutes have gone")
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)