import os
import io
import sys
import json
import time
import pydicom
import DicomSeriesCollection
import DicomDumpStripe

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("python main.py [sharedFolderName]")
        print("ex.")
        print("python main.py C:\eureka")
        sys.exit()

    inFolder = os.path.join(sys.argv[1], "input")
    outFolder = os.path.join(sys.argv[1], "output")

    dicomDump = True

    inFiles = []
    inDicomFiles = DicomSeriesCollection.DicomSeriesCollection()
    inSchemaName = 'dicom-series-in'

    for inFile in [os.path.join(root, file) for root, dir, fs in sorted(os.walk(os.path.join(inFolder, inSchemaName)))
                            for file in fs]:

        print()
        print(inFile)
        if '.dcm' in inFile:
            ds = inDicomFiles.addInstance(inFile)
            if dicomDump:
                print(ds.file_meta)
                print(ds)
        else:
            inFiles.append(inFile)

    def dumpSeries(outSchemaName, seNum, className, classAttributes):
        seriesUid, series = inDicomFiles.next()

        dstFolder = os.path.join(outFolder, outSchemaName)
        os.makedirs(dstFolder, exist_ok=True)
         
        for ins in series:
            newds = DicomDumpStripe.DicomDumpStripe.do(ins['dataset'], seNum, outSchemaName)

            dstFolderIns = dstFolder
            dstFile = os.path.join(dstFolderIns, newds.SOPInstanceUID + ".dcm") 

            if className == "sc" :
                print("This instance doesn't have pixel data. SC creation are skipped.")
            else:
                newds.save_as(dstFile)

    seriesNumber = 100
    multiple = 0
    seriesFolderRequired = True
    inDicomFiles.reset() # Reset the current pointer

    for i in range(0, multiple if multiple > 0 else len(inDicomFiles.collection)):
        dumpSeries("dicom-series-out", 
                    seriesNumber, 
                    "all", 
                    "")