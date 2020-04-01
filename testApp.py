import os


home_dir = os.system("pytest test/configuration/testConfiguration.py test/extractors/testCsvExtractor.py "
                     "test/extractors/testSpiderWebScrapperExtractor.py ")
