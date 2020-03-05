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


class TeamEditForm(object):
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
        'name': 'str',
        'teamlead': 'int',
        'users': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'teamlead': 'teamlead',
        'users': 'users'
    }

    def __init__(self, name=None, teamlead=None, users=None):  # noqa: E501
        """TeamEditForm - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._teamlead = None
        self._users = None
        self.discriminator = None

        self.name = name
        self.teamlead = teamlead
        self.users = users

    @property
    def name(self):
        """Gets the name of this TeamEditForm.  # noqa: E501

        Name of the new team  # noqa: E501

        :return: The name of this TeamEditForm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamEditForm.

        Name of the new team  # noqa: E501

        :param name: The name of this TeamEditForm.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def teamlead(self):
        """Gets the teamlead of this TeamEditForm.  # noqa: E501

        User ID for the teamlead  # noqa: E501

        :return: The teamlead of this TeamEditForm.  # noqa: E501
        :rtype: int
        """
        return self._teamlead

    @teamlead.setter
    def teamlead(self, teamlead):
        """Sets the teamlead of this TeamEditForm.

        User ID for the teamlead  # noqa: E501

        :param teamlead: The teamlead of this TeamEditForm.  # noqa: E501
        :type: int
        """
        if teamlead is None:
            raise ValueError("Invalid value for `teamlead`, must not be `None`")  # noqa: E501

        self._teamlead = teamlead

    @property
    def users(self):
        """Gets the users of this TeamEditForm.  # noqa: E501


        :return: The users of this TeamEditForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this TeamEditForm.


        :param users: The users of this TeamEditForm.  # noqa: E501
        :type: list[str]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

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
        if issubclass(TeamEditForm, dict):
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
        if not isinstance(other, TeamEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
