"""
This component provides carbon emissions .

"""

import logging
import voluptuous as vol
from distutils import util
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.service import verify_domain_control
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.exceptions import HomeAssistantError
import asyncio

from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
)

from .const import (
    COMPONENT_DOMAIN,
    COMPONENT_SERVICES
)

from homeassistant.helpers.typing import ConfigType

__version__ = '0.8.0.1'

_LOGGER = logging.getLogger(__name__)

SERVICE_AVAILABILE = 'set_available'
SERVICE_SCHEMA = vol.Schema({
    vol.Required(ATTR_ENTITY_ID): cv.comp_entity_ids,
    vol.Required('value'): cv.boolean,
})


# async def print_services(hass):
#     result = await hass.services.services()
#     _LOGGER.warning(result)



def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initialize thecomponent."""
    _LOGGER.warning("bonjour, je suis le carbone")
    result = hass.services.services
    for k,v in result.items():
        _LOGGER.warning(str(k) + " " + str(v))
    return True

# def get_entity_from_domain(hass, domain, entity_id):
#     component = hass.data.get(domain)
#     if component is None:
#         raise HomeAssistantError("{} component not set up".format(domain))

#     entity = component.get_entity(entity_id)
#     if entity is None:
#         raise HomeAssistantError("{} not found".format(entity_id))

#     return entity


# async def async_virtual_set_availability_service(hass, call):
#     entity_id = call.data['entity_id']
#     value = call.data['value']

#     if not type(value)==bool:
#         value = bool(util.strtobool(value))
#     domain = entity_id.split(".")[0]
#     _LOGGER.info("{} set_avilable(value={})".format(entity_id, value))
#     get_entity_from_domain(hass, domain, entity_id).set_available(value)