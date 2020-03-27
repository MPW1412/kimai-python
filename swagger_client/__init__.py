# coding: utf-8

# flake8: noqa

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.activity_api import ActivityApi
from swagger_client.api.customer_api import CustomerApi
from swagger_client.api.default_api import DefaultApi
from swagger_client.api.project_api import ProjectApi
from swagger_client.api.tag_api import TagApi
from swagger_client.api.team_api import TeamApi
from swagger_client.api.timesheet_api import TimesheetApi
from swagger_client.api.user_api import UserApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.activity import Activity
from swagger_client.models.activity_collection import ActivityCollection
from swagger_client.models.activity_edit_form import ActivityEditForm
from swagger_client.models.activity_entity import ActivityEntity
from swagger_client.models.activity_meta import ActivityMeta
from swagger_client.models.activity_meta_field import ActivityMetaField
from swagger_client.models.activity_rate import ActivityRate
from swagger_client.models.activity_rate_form import ActivityRateForm
from swagger_client.models.body import Body
from swagger_client.models.body1 import Body1
from swagger_client.models.body2 import Body2
from swagger_client.models.body3 import Body3
from swagger_client.models.body4 import Body4
from swagger_client.models.customer import Customer
from swagger_client.models.customer2 import Customer2
from swagger_client.models.customer_collection import CustomerCollection
from swagger_client.models.customer_edit_form import CustomerEditForm
from swagger_client.models.customer_entity import CustomerEntity
from swagger_client.models.customer_meta import CustomerMeta
from swagger_client.models.customer_meta_field import CustomerMetaField
from swagger_client.models.customer_rate import CustomerRate
from swagger_client.models.customer_rate_form import CustomerRateForm
from swagger_client.models.i18n_config import I18nConfig
from swagger_client.models.project import Project
from swagger_client.models.project2 import Project2
from swagger_client.models.project_collection import ProjectCollection
from swagger_client.models.project_edit_form import ProjectEditForm
from swagger_client.models.project_entity import ProjectEntity
from swagger_client.models.project_meta import ProjectMeta
from swagger_client.models.project_meta_field import ProjectMetaField
from swagger_client.models.project_rate import ProjectRate
from swagger_client.models.project_rate_form import ProjectRateForm
from swagger_client.models.tag_edit_form import TagEditForm
from swagger_client.models.tag_entity import TagEntity
from swagger_client.models.team import Team
from swagger_client.models.team2 import Team2
from swagger_client.models.team3 import Team3
from swagger_client.models.team4 import Team4
from swagger_client.models.team5 import Team5
from swagger_client.models.team_collection import TeamCollection
from swagger_client.models.team_edit_form import TeamEditForm
from swagger_client.models.team_entity import TeamEntity
from swagger_client.models.timesheet import Timesheet
from swagger_client.models.timesheet_collection import TimesheetCollection
from swagger_client.models.timesheet_config import TimesheetConfig
from swagger_client.models.timesheet_edit_form import TimesheetEditForm
from swagger_client.models.timesheet_entity import TimesheetEntity
from swagger_client.models.timesheet_meta import TimesheetMeta
from swagger_client.models.timesheet_meta2 import TimesheetMeta2
from swagger_client.models.timesheet_sub_collection import TimesheetSubCollection
from swagger_client.models.user import User
from swagger_client.models.user2 import User2
from swagger_client.models.user_collection import UserCollection
from swagger_client.models.user_create_form import UserCreateForm
from swagger_client.models.user_edit_form import UserEditForm
from swagger_client.models.user_entity import UserEntity
from swagger_client.models.version import Version
