from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .literals import (
    TEST_CASE_SUPERUSER_EMAIL, TEST_CASE_SUPERUSER_PASSWORD, TEST_CASE_SUPERUSER_USERNAME,
    TEST_CASE_GROUP_NAME, TEST_GROUP_NAME_EDITED, TEST_CASE_USER_EMAIL,
    TEST_CASE_USER_PASSWORD, TEST_CASE_USER_USERNAME, TEST_GROUP_NAME,
    TEST_USER_EMAIL, TEST_USER_USERNAME, TEST_USER_USERNAME_EDITED,
    TEST_USER_PASSWORD, TEST_USER_PASSWORD_EDITED
)


class GroupAPIViewTestMixin(object):
    def _request_test_group_create_api_view(self):
        result = self.post(
            viewname='rest_api:group-list', data={
                'name': TEST_GROUP_NAME
            }
        )
        if 'id' in result.json():
            self.test_group = Group.objects.get(pk=result.json()['id'])

        return result

    def _request_test_group_destroy_api_view(self):
        return self.delete(
            viewname='rest_api:group-detail', kwargs={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_group_list_api_view(self):
        return self.get(viewname='rest_api:group-list')

    def _request_test_group_partial_update_api_view(self):
        return self.patch(
            viewname='rest_api:group-detail', kwargs={
                'group_id': self.test_group.pk
            }, data={
                'name': TEST_GROUP_NAME_EDITED
            }
        )

    def _request_test_group_retrieve_api_view(self):
        return self.get(
            viewname='rest_api:group-detail', kwargs={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_group_update_api_view(self):
        return self.put(
            viewname='rest_api:group-detail', kwargs={
                'group_id': self.test_group.pk
            }, data={
                'name': TEST_GROUP_NAME_EDITED
            }
        )

    def _request_test_group_user_add_api_view(self):
        return self.post(
            viewname='rest_api:group-user-add', kwargs={
                'group_id': self.test_group.pk
            }, data={
                'user_id': self.test_user.pk
            }
        )

    def _request_test_group_user_list_api_view(self):
        return self.get(
            viewname='rest_api:group-user-list', kwargs={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_group_user_remove_api_view(self):
        return self.post(
            viewname='rest_api:group-user-remove', kwargs={
                'group_id': self.test_group.pk
            }, data={
                'user_id': self.test_user.pk
            }
        )


class GroupTestMixin(object):
    def _create_test_group(self):
        self.test_group = Group.objects.create(name=TEST_GROUP_NAME)

    def _edit_test_group(self):
        self.test_group.name = TEST_GROUP_NAME_EDITED
        self.test_group.save()


class GroupViewTestMixin(object):
    def _request_test_group_create_view(self):
        reponse = self.post(
            viewname='user_management:group_create', data={
                'name': TEST_GROUP_NAME
            }
        )
        self.test_group = Group.objects.filter(name=TEST_GROUP_NAME).first()
        return reponse

    def _request_test_group_delete_view(self):
        return self.post(
            viewname='user_management:group_delete', kwargs={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_group_edit_view(self):
        return self.post(
            viewname='user_management:group_edit', kwargs={
                'group_id': self.test_group.pk
            }, data={
                'name': TEST_GROUP_NAME_EDITED
            }
        )

    def _request_test_group_list_view(self):
        return self.get(viewname='user_management:group_list')

    def _request_test_group_members_view(self):
        return self.get(
            viewname='user_management:group_members', kwargs={
                'group_id': self.test_group.pk
            }
        )


class UserAPIViewTestMixin(object):
    def _request_test_user_create_api_view(self):
        result = self.post(
            viewname='rest_api:user-list', data={
                'email': TEST_USER_EMAIL, 'password': TEST_USER_PASSWORD,
                'username': TEST_USER_USERNAME,
            }
        )
        if 'id' in result.json():
            self.test_user = get_user_model().objects.get(pk=result.json()['id'])

        return result

    def _request_test_user_create_api_view_extra_data(self):
        result = self.post(
            viewname='rest_api:user-list', data={
                'email': TEST_USER_EMAIL, 'password': TEST_USER_PASSWORD,
                'username': TEST_USER_USERNAME,
                'groups_pk_list': self.test_group.pk
            }
        )

        if 'id' in result.json():
            self.test_user = get_user_model().objects.get(
                pk=result.json()['id']
            )

        return result

    def _request_test_user_destroy_api_view(self):
        return self.delete(
            viewname='rest_api:user-detail', kwargs={
                'user_id': self.test_user.pk
            }
        )

    def _request_test_user_group_add_api_view(self):
        return self.post(
            viewname='rest_api:user-group-add', kwargs={
                'user_id': self.test_user.pk
            }, data={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_user_group_list_api_view(self):
        return self.get(
            viewname='rest_api:user-group-list', kwargs={
                'user_id': self.test_user.pk
            }
        )

    def _request_test_user_group_remove_api_view(self):
        return self.post(
            viewname='rest_api:user-group-remove', kwargs={
                'user_id': self.test_user.pk
            }, data={
                'group_id': self.test_group.pk
            }
        )

    def _request_test_user_list_api_view(self):
        return self.get(viewname='rest_api:user-list')

    def _request_test_user_partial_update_api_view(self):
        return self.patch(
            viewname='rest_api:user-detail',
            kwargs={'user_id': self.test_user.pk},
            data={'username': TEST_USER_USERNAME_EDITED}
        )

    def _request_test_user_password_change_api_view(self):
        result = self.patch(
            viewname='rest_api:user-detail', kwargs={
                'user_id': self.test_user.pk
            }, data={
                'password': TEST_USER_PASSWORD_EDITED,
            }
        )

        self.test_user.cleartext_password = TEST_USER_PASSWORD_EDITED

        return result

    def _request_test_user_retrieve_api_view(self, extra_kwargs=None):
        kwargs = {
            'user_id': self.test_user.pk
        }
        if extra_kwargs:
            kwargs.update(**extra_kwargs)

        return self.get(
            viewname='rest_api:user-detail', kwargs=kwargs
        )

    def _request_test_user_update_api_view(self):
        return self.put(
            viewname='rest_api:user-detail', kwargs={
                'user_id': self.test_user.pk
            }, data={'username': TEST_USER_USERNAME_EDITED}
        )


class UserGroupAPIViewTestMixin(object):
    def _create_test_user_with_test_group(self):
        self._create_test_group()
        self._create_test_user()
        self.test_user.groups.add(self.test_group)


class UserTestCaseMixin(object):
    """
    This TestCaseMixin is used to create a user and group to execute the
    test case, these are used to just create an identity which is required by
    most of the code in the project, these are not meant to be acted upon
    (edited, deleted, etc). To create a test users or groups to modify, use
    the UserTestMixin instead and the respective test_user and test_group.
    The user and group created by this mixin will be prepended with
    _test_case_{...}. The _test_case_user and _test_case_group are meant
    to be used by other test case mixins like the ACLs test case mixin which
    adds shorthand methods to create ACL entries to test access control.
    """
    auto_login_superuser = False
    auto_login_user = True
    create_test_case_superuser = False
    create_test_case_user = True

    def setUp(self):
        super(UserTestCaseMixin, self).setUp()
        if self.create_test_case_user:
            self._create_test_case_user()
            self._create_test_case_group()
            self._test_case_group.user_set.add(self._test_case_user)

            if self.auto_login_user:
                self.login_user()

        if self.create_test_case_superuser:
            self._create_test_case_superuser()

            if self.auto_login_superuser:
                self.login_superuser()

    def tearDown(self):
        self.client.logout()
        super(UserTestCaseMixin, self).tearDown()

    def _create_test_case_group(self):
        self._test_case_group = Group.objects.create(name=TEST_CASE_GROUP_NAME)

    def _create_test_case_superuser(self):
        self._test_case_superuser = get_user_model().objects.create_superuser(
            username=TEST_CASE_SUPERUSER_USERNAME, email=TEST_CASE_SUPERUSER_EMAIL,
            password=TEST_CASE_SUPERUSER_PASSWORD
        )
        self._test_case_superuser.cleartext_password = TEST_CASE_SUPERUSER_PASSWORD

    def _create_test_case_user(self):
        self._test_case_user = get_user_model().objects.create_user(
            username=TEST_CASE_USER_USERNAME, email=TEST_CASE_USER_EMAIL,
            password=TEST_CASE_USER_PASSWORD
        )
        self._test_case_user.cleartext_password = TEST_CASE_USER_PASSWORD

    def login(self, *args, **kwargs):
        return self.client.login(*args, **kwargs)

    def login_superuser(self):
        return self.login(
            username=TEST_CASE_SUPERUSER_USERNAME,
            password=TEST_CASE_SUPERUSER_PASSWORD
        )

    def login_user(self):
        return self.login(
            username=TEST_CASE_USER_USERNAME, password=TEST_CASE_USER_PASSWORD
        )

    def logout(self):
        self.client.logout()


class UserTestMixin(object):
    def _create_test_superuser(self):
        self.test_superuser = get_user_model().objects.create_superuser(
            email=TEST_CASE_SUPERUSER_EMAIL,
            password=TEST_CASE_SUPERUSER_PASSWORD,
            username=TEST_CASE_SUPERUSER_USERNAME
        )
        self.test_superuser.cleartext_password = TEST_USER_PASSWORD

    def _create_test_user(self):
        total_test_users = len(self.test_users)
        username = '{}_{}'.format(TEST_USER_USERNAME, total_test_users)

        self.test_user = get_user_model().objects.create_user(
            username=username, email=TEST_USER_EMAIL,
            password=TEST_USER_PASSWORD
        )
        self.test_user.cleartext_password = TEST_USER_PASSWORD
        self.test_users.append(self.test_user)

    def setUp(self):
        super(UserTestMixin, self).setUp()
        self.test_users = []


class UserViewTestMixin(object):
    def _request_current_user_details_view(self):
        return self.get(viewname='user_management:current_user_details')

    def _request_test_superuser_delete_view(self):
        return self.post(
            viewname='user_management:user_delete',
            kwargs={'pk': self.test_superuser.pk}
        )

    def _request_test_superuser_detail_view(self):
        return self.get(
            viewname='user_management:user_details',
            kwargs={'pk': self.test_superuser.pk}
        )

    def _request_test_user_create_view(self):
        reponse = self.post(
            viewname='user_management:user_create', data={
                'username': TEST_USER_USERNAME,
                'password': TEST_USER_PASSWORD
            }
        )

        self.test_user = get_user_model().objects.filter(
            username=TEST_USER_USERNAME
        ).first()
        return reponse

    def _request_test_user_delete_view(self):
        return self.post(
            viewname='user_management:user_delete',
            kwargs={'pk': self.test_user.pk}
        )

    def _request_test_user_delete_multiple_view(self):
        return self.post(
            viewname='user_management:user_multiple_delete', data={
                'id_list': self.test_user.pk
            }
        )

    def _request_test_user_detail_view(self):
        return self.get(
            viewname='user_management:user_details', kwargs={
                'pk': self.test_user.pk
            }
        )

    def _request_test_user_edit_view(self):
        return self.post(
            viewname='user_management:user_edit', kwargs={
                'pk': self.test_user.pk
            }, data={
                'username': TEST_USER_USERNAME_EDITED
            }
        )

    def _request_test_user_groups_view(self):
        return self.get(
            viewname='user_management:user_groups',
            kwargs={'pk': self.test_user.pk}
        )
