from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins.models import OrgModelMixin
from common.mixins.models import CommonModelMixin


__all__ = ['Safe']


class Safe(CommonModelMixin, OrgModelMixin):
    """ 保险库: 账号的集合 (方便将账号与用户进行关联) """
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    comment = models.TextField(blank=True, null=True, verbose_name=_("Comment"))

    class Meta:
        unique_together = ('name', 'org_id')

    def __str__(self):
        return self.name
