# Eureka AI Machine API - Data Types Reference

---
## Input Reference Table
| Type         | Meaning                                    | Input Type | Notes                                     |
| ------------ | ------------------------------------------ | ---------- | ----------------------------------------- |
| DICOM Series | A Single DICOM Series                      | `folder`   |                                           |
| DICOM Study  | Multiple series in a study                 | `folder`   |                                           |
| File         | Arbitrary file for th engine               | `file`     | Examples include: logo, html footers, etc |
| License      | File containing the license for the engine | `file`     |                                           |
---
## Output Reference Table
| Type           | Meaning               | Output Type       | Notes                                                                |
| -------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| DICOM Series   | DICOM                 | `folder`          |                                                                      |
| DICOM Study    | DICOM                 | `folder`          |
| Image          | Jpeg, png             | `file`            |
| PDF            | pdf file              | `file`            |                                                                      |
| File           | file                  | `file`            |                                                                      |
| LogFile        | Label is the filename | `file`            |                                                                      |
| FindingSummary | Structure             | `structured file` | Detection, Pathology, Confidence, Criticality, Severity, Comment etc |
---
## Input Types
### DICOM Series
For input properties with `DICOM Series`, each individual SOPInstance will be in a separate file with the naming convention of ImageNumber_SOPInstanceUID, in the directory named for the property. 
#### Example of DICOM Series

| Label | Type           | Desc            |
| ----- | -------------- | --------------- |
| Head  | `DICOM series` | non-contrast CT |
Example Breakdown:
```
Base folder: /eureka/input
Series folder: Head
Image filename: imageNumber_SOPInstanceUID.dcm
```
Ending Result:
```
/eureka/input/Head/00001_2.16.840.1.113669.632.21.3513064216.471913.325442948016346610202.dcm
```     
---
### DICOM Study
For input properties with `DICOM Study`, there should be multiple `DICOM Series` defined for the study.
Each individual SOPInstance will be in a separate file, named by ImageNumber_SOPInstanceID, and organized into subdirectories named
by the configured series sub key.

##### Example DICOM Study

| Label  | Type           | Desc                                   |
| ------ | -------------- | -------------------------------------- |
| Fusion | `DICOM Study`  |                                        |
| CT     | `DICOM Series` | Modality is CT                         |
| PET    | `DICOM Series` | PET series with attenuation correction |

Example Breakdown:
```
Base folder: /eureka/input
Study folder: Fusion
Series Folder: CT,PET
Image Filename: imageNumber_SOPInstanceUID.dcm
```
Ending Result:
```
/eureka/input/Fusion/CT/00001_2.16.840.1.113669.632.21.3513064216.471913.325442948016346610202.dcm
/eureka/input/Fusion/PET/00001_2.16.840.1.113669.632.51.3123564216.54913.321348016346610202.dcm
```
---
### DICOM Study 4D
Eureka AI platform provides services for sorting 4D/multiphase data and is capable of handling
multiphase from multi-subseries or multi-series.

For multiphase In addition to the folder format of the `DICOM Series`, under the top-level folder, there will be json files describing the sorting information. The sorting file contains the following information:
```
Phase 1 [cardiac cycle/milliseconds and acquisition time]
LocationOnDisk, ImageID, PositionXYZ
LocationOndisk, ImageID, PositionXYZ
…..
Phase 2 [cardiac cycle/milliseconds and acquisition time]
LocationOnDisk, ImageID, PositionXYZ
```
---
##### Example DICOM 4D Study

| Label     | Type             | Desc                     |
| --------- | ---------------- | ------------------------ |
| CardiacMR | `DICOM Study 4D` |                          |
| EF        | `Multiphase`     | 4D for ejection fraction |
| T1        | `Multiphase`     | T1 mapping               |
| 3Chamber  | `DICOM Series`   | 3 Chamber View           |

Example Breakdown:
```
Base folder: /eureka/input
Study folder: CardiacMR
Multiphase Folder: EF,T1
Multiphase Sort files: EF-sort.json, T1-sort.json
Series Folder: 3Chamber
Image Filename: imageNumber_SOPInstanceUID.dcm
```
Ending Result:
```
/eureka/input/CardiacMR/EF-sort.json
/eureka/input/CaridacMR/T1-sort.json
/eureka/input/CardiacMR/EF/seriesUID/imageNumber_SOPInstanceUID.dcm
/eureka/input/CardiacMR/T1/seriesUID/imageNumbner_SOPInstanceUID.dcm
/eureka/input/CardiacMR/3Chamber/imageNumber_SOPInstanceUID.dcm
```
---
### File
For input properties with type `File`, the file will have the name of the key and placed in the top level folder
| Label    | Type   | Desc |
| -------- | ------ | ---- |
| logo.png | `File` |
Example Breakdown:
```
Base folder: /eureka/input
Filename: logo.png
```
Ending Result:
```
/eureka/input/logo.png
```
---
### License
For input properties with type `License`, the file will have the name of the key and placed in the top level folder
| Label        | Type      | Desc |
| ------------ | --------- | ---- |
| filename.lic | `License` |
Example Breakdown:
```
Base folder: /eureka/input
Filename: filename.lic
```
Ending Result:
```
/eureka/input/filename.lic
```
---
# Output Types
### DICOM Series
For output properties with `DICOM Series`, each individual SOPInstance will need to be placed in the directory named for the property and will be read by liaison upon completion of the run
#### Example of DICOM Series

| Label | Type           | Desc            |
| ----- | -------------- | --------------- |
| result-series-1  | `DICOM series` | non-contrast CT |
Example Breakdown:
```
Base folder: /eureka/output
Series folder: result-series-1
Image filename: imageNumber_SOPInstanceUID.dcm
```
Ending Result:
```
/eureka/output/result-series-1/00001_2.16.840.1.113669.632.21.3513064216.471913.325442948016346610202.dcm
```     
---
### DICOM Study
For output properties with `DICOM Study`, there should be multiple `DICOM Series` defined for the study.
Each individual output SOPInstance will be in a separate file and organized into subdirectories named
by the configured series sub key.

##### Example DICOM Study

| Label  | Type           | Desc                                   |
| ------ | -------------- | -------------------------------------- |
| Fusion | `DICOM Study`  |                                        |
| result-series-1     | `DICOM Series` | algorithm produced output                         |
| result-series-2    | `DICOM Series` | algorithm produced output |

Example Breakdown:
```
Base folder: /eureka/input
Study folder: Fusion
Series Folder: result-series-1,result-series-2
Image Filename: imageNumber_SOPInstanceUID.dcm
```
Ending Result:
```
/eureka/input/Fusion/result-series-1/00001_2.16.840.1.113669.632.21.3513064216.471913.325442948016346610202.dcm
/eureka/input/Fusion/result-series-2/00001_2.16.840.1.113669.632.51.3123564216.54913.321348016346610202.dcm
```
---
### Image
For output properties with type `Image`, the file will have the name of the key and placed in the top level folder
| Label    | Type   | Desc |
| -------- | ------ | ---- |
| result.jpeg | `Image` |
Example Breakdown:
```
Base folder: /eureka/output
Filename: result.jpeg
```
Ending Result:
```
/eureka/output/result.jpeg
```
---
### Pdf
For output properties with type `Pdf`, the file will have the name of the key and placed in the top level folder
| Label    | Type   | Desc |
| -------- | ------ | ---- |
| report.pdf | `Pdf` |
Example Breakdown:
```
Base folder: /eureka/output
Filename: report.pdf
```
Ending Result:
```
/eureka/output/report.pdf
```
---
### File
For output properties with type `File`, the file will have the name of the key and placed in the top level folder
| Label    | Type   | Desc |
| -------- | ------ | ---- |
| result-file.zip | `File` |
Example Breakdown:
```
Base folder: /eureka/output
Filename: result-file.zip
```
Ending Result:
```
/eureka/output/result-file.zip
```
---
### LogFile
For output properties with type `LogFile`, the file will have the name of the key and placed in the top level folder
| Label    | Type   | Desc |
| -------- | ------ | ---- |
| logfilename.log | `LogFile` |
Example Breakdown:
```
Base folder: /eureka/output
Filename: logfilename.log
```
Ending Result:
```
/eureka/output/logfilename.log
```
---
### FindingSummary
`FindingSummary` is intended to convey the most important clinical findings and technical information like confidence level of the finding or probability of pathology in a single file for use by the platform and it's consumers

| Label    | Type   | Desc |
| -------- | ------ | ---- |
| result-finding-summary | `FindingSummary` |
Example Breakdown:
```
Base folder: /eureka/output
Filename: result-finding-summary
```
Ending Result:
```
/eureka/output/result-finding-summary
```

##### FindingSummary structure
Example of all members of the FindingSummary structure:
```
Detection = hemorrhaging 
Pathology = present
Probability = 70%
Confidence = 80% 
Severity = moderate 
Criticality = 3
FindingCount = 3 
Selector = multiple
Comment = “Blood found on multiple slices”
```
An engine should always generate a single or multiple FindingSummary.
