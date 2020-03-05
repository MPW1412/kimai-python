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


class I18nConfig(object):
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
        'form_date_time': 'str',
        'form_date': 'str',
        'date_time': 'str',
        '_date': 'str',
        'time': 'str',
        'duration': 'str',
        'is24hours': 'bool'
    }

    attribute_map = {
        'form_date_time': 'formDateTime',
        'form_date': 'formDate',
        'date_time': 'dateTime',
        '_date': 'date',
        'time': 'time',
        'duration': 'duration',
        'is24hours': 'is24hours'
    }

    def __init__(self, form_date_time=None, form_date=None, date_time=None, _date=None, time=None, duration=None, is24hours=None):  # noqa: E501
        """I18nConfig - a model defined in Swagger"""  # noqa: E501

        self._form_date_time = None
        self._form_date = None
        self._date_time = None
        self.__date = None
        self._time = None
        self._duration = None
        self._is24hours = None
        self.discriminator = None

        if form_date_time is not None:
            self.form_date_time = form_date_time
        if form_date is not None:
            self.form_date = form_date
        if date_time is not None:
            self.date_time = date_time
        if _date is not None:
            self._date = _date
        if time is not None:
            self.time = time
        if duration is not None:
            self.duration = duration
        if is24hours is not None:
            self.is24hours = is24hours

    @property
    def form_date_time(self):
        """Gets the form_date_time of this I18nConfig.  # noqa: E501


        :return: The form_date_time of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self._form_date_time

    @form_date_time.setter
    def form_date_time(self, form_date_time):
        """Sets the form_date_time of this I18nConfig.


        :param form_date_time: The form_date_time of this I18nConfig.  # noqa: E501
        :type: str
        """

        self._form_date_time = form_date_time

    @property
    def form_date(self):
        """Gets the form_date of this I18nConfig.  # noqa: E501


        :return: The form_date of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self._form_date

    @form_date.setter
    def form_date(self, form_date):
        """Sets the form_date of this I18nConfig.


        :param form_date: The form_date of this I18nConfig.  # noqa: E501
        :type: str
        """

        self._form_date = form_date

    @property
    def date_time(self):
        """Gets the date_time of this I18nConfig.  # noqa: E501


        :return: The date_time of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this I18nConfig.


        :param date_time: The date_time of this I18nConfig.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def _date(self):
        """Gets the _date of this I18nConfig.  # noqa: E501


        :return: The _date of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this I18nConfig.


        :param _date: The _date of this I18nConfig.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def time(self):
        """Gets the time of this I18nConfig.  # noqa: E501


        :return: The time of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this I18nConfig.


        :param time: The time of this I18nConfig.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def duration(self):
        """Gets the duration of this I18nConfig.  # noqa: E501


        :return: The duration of this I18nConfig.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this I18nConfig.


        :param duration: The duration of this I18nConfig.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def is24hours(self):
        """Gets the is24hours of this I18nConfig.  # noqa: E501


        :return: The is24hours of this I18nConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is24hours

    @is24hours.setter
    def is24hours(self, is24hours):
        """Sets the is24hours of this I18nConfig.


        :param is24hours: The is24hours of this I18nConfig.  # noqa: E501
        :type: bool
        """

        self._is24hours = is24hours

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
        if issubclass(I18nConfig, dict):
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
        if not isinstance(other, I18nConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other