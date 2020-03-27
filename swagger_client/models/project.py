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


class Project(object):
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
        'name': 'str',
        'comment': 'str',
        'visible': 'bool',
        'order_number': 'str',
        'order_date': 'datetime',
        'color': 'str',
        'budget': 'float',
        'time_budget': 'int',
        'customer': 'int',
        'meta_fields': 'list[ProjectMeta]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'comment': 'comment',
        'visible': 'visible',
        'order_number': 'orderNumber',
        'order_date': 'orderDate',
        'color': 'color',
        'budget': 'budget',
        'time_budget': 'timeBudget',
        'customer': 'customer',
        'meta_fields': 'metaFields'
    }

    def __init__(self, id=None, name=None, comment=None, visible=None, order_number=None, order_date=None, color=None, budget=None, time_budget=None, customer=None, meta_fields=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._comment = None
        self._visible = None
        self._order_number = None
        self._order_date = None
        self._color = None
        self._budget = None
        self._time_budget = None
        self._customer = None
        self._meta_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if comment is not None:
            self.comment = comment
        self.visible = visible
        if order_number is not None:
            self.order_number = order_number
        if order_date is not None:
            self.order_date = order_date
        if color is not None:
            self.color = color
        self.budget = budget
        self.time_budget = time_budget
        if customer is not None:
            self.customer = customer
        if meta_fields is not None:
            self.meta_fields = meta_fields

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 150:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")  # noqa: E501
        if name is not None and len(name) < 2:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `2`")  # noqa: E501

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this Project.  # noqa: E501


        :return: The comment of this Project.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Project.


        :param comment: The comment of this Project.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def visible(self):
        """Gets the visible of this Project.  # noqa: E501


        :return: The visible of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this Project.


        :param visible: The visible of this Project.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def order_number(self):
        """Gets the order_number of this Project.  # noqa: E501


        :return: The order_number of this Project.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Project.


        :param order_number: The order_number of this Project.  # noqa: E501
        :type: str
        """
        if order_number is not None and len(order_number) > 20:
            raise ValueError("Invalid value for `order_number`, length must be less than or equal to `20`")  # noqa: E501

        self._order_number = order_number

    @property
    def order_date(self):
        """Gets the order_date of this Project.  # noqa: E501


        :return: The order_date of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this Project.


        :param order_date: The order_date of this Project.  # noqa: E501
        :type: datetime
        """

        self._order_date = order_date

    @property
    def color(self):
        """Gets the color of this Project.  # noqa: E501


        :return: The color of this Project.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Project.


        :param color: The color of this Project.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def budget(self):
        """Gets the budget of this Project.  # noqa: E501


        :return: The budget of this Project.  # noqa: E501
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this Project.


        :param budget: The budget of this Project.  # noqa: E501
        :type: float
        """
        if budget is None:
            raise ValueError("Invalid value for `budget`, must not be `None`")  # noqa: E501

        self._budget = budget

    @property
    def time_budget(self):
        """Gets the time_budget of this Project.  # noqa: E501


        :return: The time_budget of this Project.  # noqa: E501
        :rtype: int
        """
        return self._time_budget

    @time_budget.setter
    def time_budget(self, time_budget):
        """Sets the time_budget of this Project.


        :param time_budget: The time_budget of this Project.  # noqa: E501
        :type: int
        """
        if time_budget is None:
            raise ValueError("Invalid value for `time_budget`, must not be `None`")  # noqa: E501

        self._time_budget = time_budget

    @property
    def customer(self):
        """Gets the customer of this Project.  # noqa: E501


        :return: The customer of this Project.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Project.


        :param customer: The customer of this Project.  # noqa: E501
        :type: int
        """

        self._customer = customer

    @property
    def meta_fields(self):
        """Gets the meta_fields of this Project.  # noqa: E501


        :return: The meta_fields of this Project.  # noqa: E501
        :rtype: list[ProjectMeta]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this Project.


        :param meta_fields: The meta_fields of this Project.  # noqa: E501
        :type: list[ProjectMeta]
        """

        self._meta_fields = meta_fields

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
