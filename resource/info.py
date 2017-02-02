from BaseClass import WaterBase
class Info(WaterBase):
    def get(self):
        return "This API has the following Endpoints: \n" \
               "setGroup<DeviceID/GroupName>" \
               "sets a device as member of the specified group \n" \
               "getGroup/<DeviceID>" \
               "see which group the device has been member of" \
               "groupInfo<GroupName, Timestamp>" \
               "gets all datasets for the specified group from timestamp up to the days specified. \n" \
               "if no day is specified: days = 4" \
               ""
