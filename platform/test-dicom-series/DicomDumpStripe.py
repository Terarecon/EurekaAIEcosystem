import copy
import pydicom
import Buffer
import InstanceUidBuilder

class DicomDumpStripe:

    seriesUidDictionary = {}
    sopUidDictionary = []

    def do(ds, seriesNumber, message):
    
        ds = copy.deepcopy(ds)

        if "PixelData" in ds:

            pixels = ds.pixel_array
            width = pixels.shape[0]
            height = pixels.shape[1]

            step = 16

            if width > step:
                for x in range(0, width, int(width / step)):
                    Buffer.drawLine(pixels, x, 0, x, height - 1, 2048)

            if height > step:
                for y in range(0, height, int(height / step)):
                    Buffer.drawLine(pixels, 0, y, width - 1, y, 2048)

            Buffer.drawString(pixels, 0, 0, 2, message, 2048)

            ds.PixelData = pixels.tobytes()

        newSeUid = DicomDumpStripe.seriesUidDictionary[seriesNumber] if seriesNumber in DicomDumpStripe.seriesUidDictionary else InstanceUidBuilder.InstanceUidBuilder.seriesInstanceUid(1, seriesNumber)
        DicomDumpStripe.seriesUidDictionary[seriesNumber] = newSeUid
        ds.SeriesInstanceUID = newSeUid

        newSopUID = InstanceUidBuilder.InstanceUidBuilder.sopInstanceUid(1, seriesNumber, len(DicomDumpStripe.sopUidDictionary) + 1)
        DicomDumpStripe.sopUidDictionary.append(newSopUID)
        ds.SOPInstanceUID = newSopUID
        ds.file_meta.MediaStorageSOPInstanceUID = newSopUID

        return ds
