# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GeoRegion(Model):

    _attribute_map = {
        'region_code': {'key': 'regionCode', 'type': 'str'}
    }

    def __init__(self, region_code=None):
        super(GeoRegion, self).__init__()
        self.region_code = region_code


class ProfileRegion(Model):

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, code=None, name=None):
        super(ProfileRegion, self).__init__()
        self.code = code
        self.name = name


class ProfileRegions(Model):

    _attribute_map = {
        'notice_contact_consent_requirement_regions': {'key': 'noticeContactConsentRequirementRegions', 'type': '[str]'},
        'opt_out_contact_consent_requirement_regions': {'key': 'optOutContactConsentRequirementRegions', 'type': '[str]'},
        'regions': {'key': 'regions', 'type': '[ProfileRegion]'}
    }

    def __init__(self, notice_contact_consent_requirement_regions=None, opt_out_contact_consent_requirement_regions=None, regions=None):
        super(ProfileRegions, self).__init__()
        self.notice_contact_consent_requirement_regions = notice_contact_consent_requirement_regions
        self.opt_out_contact_consent_requirement_regions = opt_out_contact_consent_requirement_regions
        self.regions = regions


__all__ = [
    'GeoRegion',
    'ProfileRegion',
    'ProfileRegions',
]
