# get-heart-rate-csv

A small Python script to get the heart rate data generated from an Apple Watch in a CSV form, using the official export XML dump. This CSV can then be used in other statistical applications for easy analysis.

## Usage

Generate an export of your HealthKit data on your iPhone. Then move the `hr_xml_to_csv.py` script into the folder and run.

The output will be a CSV with 2 columns: a `dt` which contains the datetime of of the heart rate measurement, and `bpm` representing the measurement itself.

## Maintainer

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT