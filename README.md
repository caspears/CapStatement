# CapStatement
FHIR CapabilityStatement generation via python script and Jinja template

Modified from: Eric Haas tool available at: https://github.com/Healthedata1/MyNotebooks/blob/master/CapStatement/R4CapStatement_Maker.ipynb

This tool is mostly adaptations of Eric's great original work.

# Integrated IG Publisher Version
There is a liquid template version of this capabilityStatement narrative generator that can work in line with the FHIR IG Publisher. 
To use:
- Copy the liquid folder into the IG base folder
- Add a parameter to your ImplementationGuide resource or sushi-config.yaml

  Example in sushi-config
```
parameters:   
  path-liquid: liquid
```
Example Implementation Guide parameter
```
"extension": [
  {
    "extension": [
      {
        "url": "code",
        "valueString": "path-liquid"
      },
      {
        "url": "value",
        "valueString": "liquid"
      }
    ],
    "url": "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
  }
]
```

- Build the IG

# Python Script Narrative Rendering Version
## Getting Started

Dependecies: 
    fhirclient 
    pandas
    xlrd
    openpyxl
    stringcase
    jinja2
    commonmark
    lxml


To install all dependencies: `pip3 install -r requirements.txt`
to run on windows: `python -m pip ...`

NOTE: fhirclient can be installed via pip or copied from this repository (note that fhirclient is not being maintained in this respository)
The fhirclient requires the r4models to be installed (also included in this repository in the fhirclient folder. These modified R4 models need to be installed with the fhirclient pip site-package in [installdir]/lib/python/site-packages/fhirclient


## Generate CapabilityStatement with Narrative from xslx file

Usage: `python3 R4CapStatement_Maker.py [xlsx file]`

## Generate CapabilityStatement Narrative from existing CapabilityStatement

Usage: `python3 R4CapStatement_NarrativeMaker.py [json file (wildcards supported)] {[Artifacts Folder]}`

Currently creates a new CapabilityStatement json file prefixed with "Narrative-" 

Wildcards for json file name will iterate on all matches (i.e. support for generating narratives for multiple CapabilityStatement files at the same time)

Artifacts folder is optional. It is the location of the locally (pre)built FHIR IG artifacts (output folder). This is used to retrieve the names (title) of artifacts to use as the link text in the generated narrative. 
For any artifacts for which a name was not retrieved (e.g. no artifact folder provided or externally defined references), the script will attempt to retrieve the artifact (and name) using the artifact's specified url.


## Future Plans

Clean up beyond quick and dirty tool.

Merge the two scripts into one script.

Potentially merge with other tooling (including from Eric Haas) to create a single toolset.
