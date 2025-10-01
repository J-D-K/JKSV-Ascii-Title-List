#!/usr/bin/python3
# coding: utf-8

import sys
import json

def main() -> int:
    # This is what JKSV saves its paths to.
    inputPath: str = "./Paths.json"
    # This is the end result.
    outputPath: str = "./MasterList.json"

    with open(file=inputPath, mode="r") as inputFile:
        inputData: str = inputFile.read()

    with open(file=outputPath, mode="r") as outputFile:
        outputData: str = outputFile.read()

    inputJson: dict[str, str]  = json.loads(s=inputData)
    outputJson: dict[str, str] = json.loads(s=outputData)

    for applicationID, path in inputJson.items():
        
        if outputJson.get(applicationID) != None:
            print(f"{applicationID}: {path} -> Already Exists")
            continue
        
        outputJson[applicationID] = path
        print(f"{applicationID}: {path} -> Added to MasterList")

    with open(outputPath, "w") as outputFile:
        json.dump(obj=outputJson, fp=outputFile, indent=4)

    return 0

if __name__ == "__main__":
    sys.exit(main())