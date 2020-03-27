# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TimesheetEntity(object):
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
        'id': 'int',
        'duration': 'int',
        'rate': 'float',
        'description': 'str',
        'fixed_rate': 'float',
        'hourly_rate': 'float',
        'exported': 'bool',
        'begin': 'datetime',
        'end': 'datetime',
        'activity': 'int',
        'project': 'int',
        'user': 'int',
        'tags': 'list[str]',
        'meta_fields': 'list[TimesheetMeta2]',
        'internal_rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'duration': 'duration',
        'rate': 'rate',
        'description': 'description',
        'fixed_rate': 'fixedRate',
        'hourly_rate': 'hourlyRate',
        'exported': 'exported',
        'begin': 'begin',
        'end': 'end',
        'activity': 'activity',
        'project': 'project',
        'user': 'user',
        'tags': 'tags',
        'meta_fields': 'metaFields',
        'internal_rate': 'internalRate'
    }

    def __init__(self, id=None, duration=None, rate=None, description=None, fixed_rate=None, hourly_rate=None, exported=None, begin=None, end=None, activity=None, project=None, user=None, tags=None, meta_fields=None, internal_rate=None):  # noqa: E501
        """TimesheetEntity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._duration = None
        self._rate = None
        self._description = None
        self._fixed_rate = None
        self._hourly_rate = None
        self._exported = None
        self._begin = None
        self._end = None
        self._activity = None
        self._project = None
        self._user = None
        self._tags = None
        self._meta_fields = None
        self._internal_rate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if duration is not None:
            self.duration = duration
        if rate is not None:
            self.rate = rate
        if description is not None:
            self.description = description
        if fixed_rate is not None:
            self.fixed_rate = fixed_rate
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        self.exported = exported
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end
        if activity is not None:
            self.activity = activity
        if project is not None:
            self.project = project
        if user is not None:
            self.user = user
        if tags is not None:
            self.tags = tags
        if meta_fields is not None:
            self.meta_fields = meta_fields
        if internal_rate is not None:
            self.internal_rate = internal_rate

    @property
    def id(self):
        """Gets the id of this TimesheetEntity.  # noqa: E501


        :return: The id of this TimesheetEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimesheetEntity.


        :param id: The id of this TimesheetEntity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def duration(self):
        """Gets the duration of this TimesheetEntity.  # noqa: E501


        :return: The duration of this TimesheetEntity.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimesheetEntity.


        :param duration: The duration of this TimesheetEntity.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def rate(self):
        """Gets the rate of this TimesheetEntity.  # noqa: E501


        :return: The rate of this TimesheetEntity.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this TimesheetEntity.


        :param rate: The rate of this TimesheetEntity.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def description(self):
        """Gets the description of this TimesheetEntity.  # noqa: E501


        :return: The description of this TimesheetEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimesheetEntity.


        :param description: The description of this TimesheetEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fixed_rate(self):
        """Gets the fixed_rate of this TimesheetEntity.  # noqa: E501


        :return: The fixed_rate of this TimesheetEntity.  # noqa: E501
        :rtype: float
        """
        return self._fixed_rate

    @fixed_rate.setter
    def fixed_rate(self, fixed_rate):
        """Sets the fixed_rate of this TimesheetEntity.


        :param fixed_rate: The fixed_rate of this TimesheetEntity.  # noqa: E501
        :type: float
        """

        self._fixed_rate = fixed_rate

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this TimesheetEntity.  # noqa: E501


        :return: The hourly_rate of this TimesheetEntity.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this TimesheetEntity.


        :param hourly_rate: The hourly_rate of this TimesheetEntity.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def exported(self):
        """Gets the exported of this TimesheetEntity.  # noqa: E501


        :return: The exported of this TimesheetEntity.  # noqa: E501
        :rtype: bool
        """
        return self._exported

    @exported.setter
    def exported(self, exported):
        """Sets the exported of this TimesheetEntity.


        :param exported: The exported of this TimesheetEntity.  # noqa: E501
        :type: bool
        """
        if exported is None:
            raise ValueError("Invalid value for `exported`, must not be `None`")  # noqa: E501

        self._exported = exported

    @property
    def begin(self):
        """Gets the begin of this TimesheetEntity.  # noqa: E501


        :return: The begin of this TimesheetEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this TimesheetEntity.


        :param begin: The begin of this TimesheetEntity.  # noqa: E501
        :type: datetime
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this TimesheetEntity.  # noqa: E501


        :return: The end of this TimesheetEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TimesheetEntity.


        :param end: The end of this TimesheetEntity.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def activity(self):
        """Gets the activity of this TimesheetEntity.  # noqa: E501


        :return: The activity of this TimesheetEntity.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TimesheetEntity.


        :param activity: The activity of this TimesheetEntity.  # noqa: E501
        :type: int
        """

        self._activity = activity

    @property
    def project(self):
        """Gets the project of this TimesheetEntity.  # noqa: E501


        :return: The project of this TimesheetEntity.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TimesheetEntity.


        :param project: The project of this TimesheetEntity.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def user(self):
        """Gets the user of this TimesheetEntity.  # noqa: E501


        :return: The user of this TimesheetEntity.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TimesheetEntity.


        :param user: The user of this TimesheetEntity.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def tags(self):
        """Gets the tags of this TimesheetEntity.  # noqa: E501


        :return: The tags of this TimesheetEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TimesheetEntity.


        :param tags: The tags of this TimesheetEntity.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def meta_fields(self):
        """Gets the meta_fields of this TimesheetEntity.  # noqa: E501


        :return: The meta_fields of this TimesheetEntity.  # noqa: E501
        :rtype: list[TimesheetMeta2]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this TimesheetEntity.


        :param meta_fields: The meta_fields of this TimesheetEntity.  # noqa: E501
        :type: list[TimesheetMeta2]
        """

        self._meta_fields = meta_fields

    @property
    def internal_rate(self):
        """Gets the internal_rate of this TimesheetEntity.  # noqa: E501


        :return: The internal_rate of this TimesheetEntity.  # noqa: E501
        :rtype: float
        """
        return self._internal_rate

    @internal_rate.setter
    def internal_rate(self, internal_rate):
        """Sets the internal_rate of this TimesheetEntity.


        :param internal_rate: The internal_rate of this TimesheetEntity.  # noqa: E501
        :type: float
        """

        self._internal_rate = internal_rate

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
        if issubclass(TimesheetEntity, dict):
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
        if not isinstance(other, TimesheetEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
