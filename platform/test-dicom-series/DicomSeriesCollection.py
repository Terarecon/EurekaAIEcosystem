import os
import io
import sys
import pydicom

class DicomSeriesCollection:

    class DicomInstanceCollection:
        def __init__(self):
            self.collection = []

        def append(self, sopUid, file, dataset):
            self.collection.append({'uid': sopUid, 'file': file, 'dataset': dataset})
    
        def __iter__(self):
            return self.collection.__iter__()

        def __next__(self):
            return self.collection.__next__()

    def __init__(self):
        self.collection = {}
        self.current = 0

    def addInstance(self, filename):

        ds = pydicom.dcmread(filename)
        seriesUid = ds.SeriesInstanceUID
        sopUid = ds.SOPInstanceUID
        if not seriesUid in self.collection:
            self.collection[seriesUid] = DicomSeriesCollection.DicomInstanceCollection()
        
        self.collection[seriesUid].append(sopUid, filename, ds)

        return ds

    def next(self):
        if self.current == len(self.collection):
            self.current = 0;

        key = list(self.collection)[self.current]
        self.current += 1
        return key, self.collection[key]
    
    def reset(self):
        self.current = 0;





