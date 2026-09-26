init -1 python:
    class DressCode:
        def __init__(self, code, name, priority, characters):
            self.code = code
            self.name = name
            self.priority = priority
            self.characters = characters
            self.location = False
            self.sublocation = False
            self.position = False
            self.timeslots = False
            self.days = False
    
        @staticmethod
        def init_dress_code(code):
            dress_code_data = DRESS_CODE_CATALOGUE[code]
            dress_code_object = DressCode(code, dress_code_data[NAME], dress_code_data[PRIORITY], dress_code_data[CHARACTERS])
            dress_code_object.location = dress_code_data.get(LOCATION, False)
            dress_code_object.sublocation = dress_code_data.get(SUBLOCATION, False)
            dress_code_object.position = dress_code_data.get(POSITION, False)
            dress_code_object.timeslots = dress_code_data.get(TIMESLOTS, False)
            dress_code_object.days = dress_code_data.get(DAYS, False)
            return dress_code_object

    class DressCodeController:
    
        @staticmethod
        def add_dress_code(code):
            if not hasattr(renpy.store, "SM_DRESS_CODE_LIST"):
                setattr(renpy.store, "SM_DRESS_CODE_LIST", [])
            dress_codes = getattr(renpy.store, "SM_DRESS_CODE_LIST")
            if code not in [dc.code for dc in dress_codes]:
                dress_codes.append(DressCode.init_dress_code(code))
            setattr(renpy.store, "SM_DRESS_CODE_LIST", dress_codes)
    
        @staticmethod
        def initialize_persistent_dress_codes():
            for code in PERSISTENT_DRESS_CODES:
                DressCodeController.add_dress_code(code)
    
        @staticmethod
        def get_dress_code(character, timeslot, day, location, sublocation, position):
            if not hasattr(renpy.store, "SM_DRESS_CODE_LIST"):
                setattr(renpy.store, "SM_DRESS_CODE_LIST", [])
        
            dress_codes = getattr(renpy.store, "SM_DRESS_CODE_LIST")
            matching_dress_codes = []
        
            for dress_code in dress_codes:
                if (ALL in dress_code.characters or character in dress_code.characters) and \
                    (not dress_code.location or location in dress_code.location) and \
                    (not dress_code.sublocation or sublocation in dress_code.sublocation) and \
                    (not dress_code.position or position in dress_code.position) and \
                    (not dress_code.timeslots or timeslot in dress_code.timeslots) and \
                    (not dress_code.days or day in dress_code.days):
                        matching_dress_codes.append({NAME: dress_code.name, PRIORITY: dress_code.priority})
        
            if matching_dress_codes:
                priority_dress_code = max(matching_dress_codes, key=lambda x: x[PRIORITY])
                return priority_dress_code[NAME]
            return False
