# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen, but we try to avoid them.   # noqa: E501

    OpenAPI spec version: 0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserCreateForm(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str',
        'alias': 'str',
        'title': 'str',
        'avatar': 'str',
        'email': 'str',
        'language': 'str',
        'timezone': 'str',
        'enabled': 'bool',
        'plain_password': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'alias': 'alias',
        'title': 'title',
        'avatar': 'avatar',
        'email': 'email',
        'language': 'language',
        'timezone': 'timezone',
        'enabled': 'enabled',
        'plain_password': 'plainPassword',
        'roles': 'roles'
    }

    def __init__(self, username=None, alias=None, title=None, avatar=None, email=None, language=None, timezone=None, enabled=None, plain_password=None, roles=None):  # noqa: E501
        """UserCreateForm - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._alias = None
        self._title = None
        self._avatar = None
        self._email = None
        self._language = None
        self._timezone = None
        self._enabled = None
        self._plain_password = None
        self._roles = None
        self.discriminator = None

        self.username = username
        if alias is not None:
            self.alias = alias
        if title is not None:
            self.title = title
        if avatar is not None:
            self.avatar = avatar
        self.email = email
        self.language = language
        self.timezone = timezone
        if enabled is not None:
            self.enabled = enabled
        self.plain_password = plain_password
        if roles is not None:
            self.roles = roles

    @property
    def username(self):
        """Gets the username of this UserCreateForm.  # noqa: E501


        :return: The username of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserCreateForm.


        :param username: The username of this UserCreateForm.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def alias(self):
        """Gets the alias of this UserCreateForm.  # noqa: E501


        :return: The alias of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UserCreateForm.


        :param alias: The alias of this UserCreateForm.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def title(self):
        """Gets the title of this UserCreateForm.  # noqa: E501


        :return: The title of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserCreateForm.


        :param title: The title of this UserCreateForm.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def avatar(self):
        """Gets the avatar of this UserCreateForm.  # noqa: E501


        :return: The avatar of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this UserCreateForm.


        :param avatar: The avatar of this UserCreateForm.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def email(self):
        """Gets the email of this UserCreateForm.  # noqa: E501


        :return: The email of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserCreateForm.


        :param email: The email of this UserCreateForm.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def language(self):
        """Gets the language of this UserCreateForm.  # noqa: E501


        :return: The language of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UserCreateForm.


        :param language: The language of this UserCreateForm.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        allowed_values = ["ar", "cs", "de", "de_CH", "da", "en", "es", "eu", "fr", "hu", "it", "ja", "ko", "nl", "pl", "pt_BR", "ru", "sk", "sv", "tr", "zh_CN"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this UserCreateForm.  # noqa: E501


        :return: The timezone of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserCreateForm.


        :param timezone: The timezone of this UserCreateForm.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def enabled(self):
        """Gets the enabled of this UserCreateForm.  # noqa: E501


        :return: The enabled of this UserCreateForm.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserCreateForm.


        :param enabled: The enabled of this UserCreateForm.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def plain_password(self):
        """Gets the plain_password of this UserCreateForm.  # noqa: E501

        Plain text password  # noqa: E501

        :return: The plain_password of this UserCreateForm.  # noqa: E501
        :rtype: str
        """
        return self._plain_password

    @plain_password.setter
    def plain_password(self, plain_password):
        """Sets the plain_password of this UserCreateForm.

        Plain text password  # noqa: E501

        :param plain_password: The plain_password of this UserCreateForm.  # noqa: E501
        :type: str
        """
        if plain_password is None:
            raise ValueError("Invalid value for `plain_password`, must not be `None`")  # noqa: E501

        self._plain_password = plain_password

    @property
    def roles(self):
        """Gets the roles of this UserCreateForm.  # noqa: E501


        :return: The roles of this UserCreateForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserCreateForm.


        :param roles: The roles of this UserCreateForm.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ROLE_TEAMLEAD", "ROLE_ADMIN", "ROLE_SUPER_ADMIN"]  # noqa: E501
        if not set(roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserCreateForm, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserCreateForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
