from collections import namedtuple
from configparser import ConfigParser, DEFAULTSECT

from .load import base_path

parser = ConfigParser()
tracked_classes = []
prop_attribs = namedtuple('prop_attribs', 'config_name required section')
all_props = []
attr_map = {}
_UNSET = object()
has_read = False
config_file = str(base_path / 'config.ini')


def load_config():
    global has_read
    if not has_read:
        parser.read(config_file)
        has_read = True


def prop_name(section, option):
    return (section + '.' if section and section != DEFAULTSECT else '') + option


def section(section_name: str):
    def x(c):
        tracked_classes.append(c)
        c._section = section_name
        c._props = []
        for p in dir(c):
            prop = getattr(c, p)
            try:
                prop = attr_map.get(prop, prop)
            except:
                continue
            if hasattr(prop, 'config_name'):
                s = prop.section or section_name
                prop_info = prop_attribs(prop.config_name, prop.required, s)
                c._props.append(prop_info)
                all_props.append(prop_info)
        return c()

    return x


def create_property(name, conv, section, fallback):
    def get(self):
        load_config()
        s = section or getattr(self, '_section', None) or DEFAULTSECT
        cv = parser.get(s, name, fallback=fallback)
        if cv is _UNSET:
            raise ValueError("Missing config option")
        else:
            return conv(cv)

    p = property(get)
    attrs = prop_attribs(name, fallback is _UNSET, section)
    attr_map[p] = attrs
    return p


def required(name: str, conv=str, section=None):
    return create_property(name, conv, section, _UNSET)


def default(name: str, default_value, conv=str, section=None):
    return create_property(name, conv, section, default_value)


def prompt_missing_configs():
    load_config()
    for p in all_props:
        if parser.get(p.section, p.config_name, fallback=_UNSET) is _UNSET:
            if not parser.has_section(p.section):
                parser.add_section(p.section)
            parser.set(p.section, p.config_name,
                       input(f"What value do you want for {prop_name(p.section, p.config_name)}: "))
    with open(config_file, 'w') as fp:
        parser.write(fp)
    print('Wrote config.ini')


__all__ = ['default', 'required', 'section', 'prompt_missing_configs']
