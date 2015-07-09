import enum

class ChoicesEnumMeta(type(enum.Enum)):
    def __new__(metacls, cls, bases, classdict):
        if type(classdict) is dict:
            original_dict = classdict
            classdict = enum._EnumDict()
            for k, v in original_dict.items():
                classdict[k] = v

        if '__getitem__'  not in classdict:
            classdict['__getitem__'] = lambda self, idx: [self.value, self.display][idx]
        if '__len__' not in classdict:
            classdict['__len__'] = lambda self: 2

        return super(ChoicesEnumMeta, metacls).__new__(metacls, cls, bases, classdict)

    @staticmethod
    def _find_new_(classdict, obj_type, first_enum):
        def new(enum_class, db, display=None):
            real_new, save_new, use_args = type(enum.Enum)._find_new_(classdict, obj_type, first_enum)
            if not use_args:
                enum_item = real_new(enum_class)
                enum_item._value_ = db
            else:
                enum_item = real_new(enum_class, db)
                if not hasattr(enum_item, '_value'):
                    enum_item._value_ = obj_type(db)
            enum_item.display = display if display is not None else db
            return enum_item
        return new, False, True

class ChoicesEnum(enum.Enum):
    __metaclass__ = ChoicesEnumMeta

    @classmethod
    def choices(cls):
        return [(v.value, v.display) for _, v in cls._member_map_.items()]
