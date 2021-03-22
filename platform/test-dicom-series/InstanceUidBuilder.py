import datetime

class InstanceUidBuilder:

    seedRoot = "2.16.840" #your unique root here
    seedOccupancy = "5500"
    seedDeviceType = "1"
    seedStudyInstanceUid = "2"
    seedSeriesInstanceUid = "3"
    seedSopInstanceUid = "4"
    seedFrameOfReferenceUid = "5"

    base = seedRoot + '.' + seedOccupancy + '.' + seedDeviceType

    def dateString():

        now = datetime.datetime.now()
        return "{:04}".format(now.year) + "{:02}".format(now.month) + "{:02}".format(now.day) + "{:02}".format(now.hour) + "{:02}".format(now.minute) + "{:02}".format(now.second) + "{:03}".format(now.microsecond)

    _lastStUid = ""

    def studyInstanceUid(studyNumber):
        
        while True:
            newStUid = InstanceUidBuilder.base + '.' + InstanceUidBuilder.seedStudyInstanceUid + '.' + InstanceUidBuilder.dateString() + '.' + str(studyNumber)

            if InstanceUidBuilder._lastStUid != newStUid:
                break

        InstanceUidBuilder._lastStUid = newStUid
        return newStUid


    _lastSeUid = ""

    def seriesInstanceUid(studyNumber, seriesNumber):

        while True:
            newSeUid = InstanceUidBuilder.base + '.' + InstanceUidBuilder.seedStudyInstanceUid + '.' + InstanceUidBuilder.dateString() + '.' + str(studyNumber) + '.' + str(seriesNumber)

            if InstanceUidBuilder._lastSeUid != newSeUid:
                break

        InstanceUidBuilder._lastSeUid = newSeUid
        return newSeUid

    _lastSopUid = ""

    def sopInstanceUid(studyNumber, seriesNumber, imageNumber):

        while True:
            newSopUid = InstanceUidBuilder.base + '.' + InstanceUidBuilder.seedStudyInstanceUid + '.' + InstanceUidBuilder.dateString() + '.' + str(studyNumber) + '.' + str(seriesNumber) + '.' + str(imageNumber)

            if InstanceUidBuilder._lastSopUid != newSopUid:
                break

        InstanceUidBuilder._lastSopUid = newSopUid
        return newSopUid
