# base-tests

+## Installation
+In project directory:
+
+```
+pip3 install -r requirements.txt
+```
+
+## Usage
+
+All configuration is located in variables.json file.
+Before running tests close all first launch tutorials that appear on tested pages.
+Copy variables.json outside git repository and enter your credentials.

+## To run tests:
+
+```
+py.test --variables /path/to/variables.json

+## Tested on

+OS X 10.9.5
+chrome 44.0
+chromedriver 2.18
