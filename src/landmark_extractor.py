#!/usr/bin/env python

import json
import codecs
import argparse
from extraction.Landmark import RuleSet
from extraction.Landmark import flattenResult


def extractfeatures(input_file, extraction_rules):
    if input_file:
        try:

            html = input_file
            rules = RuleSet(extraction_rules)

            if rules is not None:
                extraction_list = rules.extract(html)
                flatten = flattenResult(extraction_list)
                return flatten
            else:
                return {}
        except Exception, e:
            print "ERRROR:", str(e)
            return {}


if __name__ == '__main__':

    argp = argparse.ArgumentParser()
    argp.add_argument("inputfile", help="input json file for the extraction")
    argp.add_argument("outputfile", help="output file, after the extraction")
    argp.add_argument("extractionrules", help="the one extraction rules file with rules for all different sources")
    arguments = argp.parse_args()

    input_file = codecs.open(arguments.inputfile, 'r', 'utf-8')
    output_file = codecs.open(arguments.outputfile, 'w', "utf-8")

    with codecs.open(arguments.extractionrules, 'r', "utf-8") as rulefile:
        extraction_rules = rulefile.read().encode('utf-8')

    j_extraction_rules = json.loads(extraction_rules)

    output_file.write(json.dumps(extractfeatures(input_file, j_extraction_rules)))

    print "Thats all folks!"
