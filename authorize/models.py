from django.db import models

from django.contrib.auth.models import User


# Menus are essential components of application that requires proper authentication from users

# name ----> user readable string representation of menu
# code ----> code which can be used as authentication string
class Menu(models.Model):

    name = models.CharField(max_length=55)

    code = models.CharField(max_length=55)

    class Meta:

        db_table = 'authorize_menu'

    def __str__(self):

        return str(self.name)

    def __unicode__(self):

        return str(self.name)


# Role handles set of privileges which can be assigned to an user

# name ----> string representation of role
class Role(models.Model):

    name = models.CharField(max_length=55)

    class Meta:

        db_table = 'authorize_role'

    def __str__(self):

        return str(self.name)

    def __unicode__(self):

        return str(self.name)


# Privilege reflects the menu access for a particular role

# role ----> each privilege has a parent role
# menu ----> each privilege has a parent menu
# access ----> flag which reflects the authentication status
class Privilege(models.Model):

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    access = models.BooleanField(default=False)

    class Meta:

        db_table = 'authorize_privilege'

    def __str__(self):

        return str(self.access)

    def __unicode__(self):

        return str(self.access)


# UserProfile is just an add-on model for user for the purpose of handling auxiliary functions

# user ----> each profile is an extension of inbuilt user model
# role ----> each profile has a parent role
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:

        db_table = 'authorize_user_profile'

    def __str__(self):

        return str(self.user.username)

    def __unicode__(self):

        return str(self.user.username)
