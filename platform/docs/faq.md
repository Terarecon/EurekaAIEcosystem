# Eureka AI Platform Frequently Asked Questions
<hr/> 
## Dev Portal

#### How do I log into the developer portal?
[https://portal.terarecon.com](https://portal.terarecon.com)

#### How do I learn how to create a machine?
The best way to learn about how to create a machine on the Eureka AI Platform is to read the [helloworld walk-through](./walkthrough.md).

#### How do I create a machine that takes a Dicom file as input?
To learn more about DICOM input and other advanced input and output types, please see [types schema specification](types.md).
To see a simple example that takes a DICOM series as input and returns a DICOM series as output,
see the [test-dicom-series](../test-dicom-series) docker example.

For an algorithm that takes a single image as either the input or the output, please use the type 'DICOM Series' as the platform will handle this appropriately 

#### How do I provide test or sample data for my machine?
For users within your organization you can upload sample data to the "Files"
tab the dev portal. These files will be available to everyone within your
dev portal account's group.

<hr/>
## Docker and Machine API

#### How do I quickly adapt an already working dockerfile?
After creating an input/output definition in the portal for your algorithm, you can adapt your docker container to take the input from the specified folders presented on the portal.

To quickly adapt your container, use the provided folder paths from the portal for your machine to parse the data for your algorithm. The input and expected result output paths are provided in full on the portal when you setup your input/output schema.

That should be all that is needed to adapt an already dockerized algorithm.

#### How do I view debugging information about my machine when its running on the platform?
All logs, captured from your executable's stdout and stderr and are available with the results of an evaluation of the machine on the portal.

#### How do I get started with Docker?
To download and install Docker please visit [docker.com](https://docker.com/get-docker)

#### Does the Eureka AI Platform Support CUDA?
The Eureka AI Platform supports nVidia CUDA 11. If your algorithm require a different version, please contact us and we will try to make it available.

#### How does the Eureka AI Platform Support de-identification
Please refer to this document [de-identification specification](EurekaAI_de-id_specification.pdf) for all de-identification following safe harbor principals on the platform