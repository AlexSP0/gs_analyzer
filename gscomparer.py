import gsanalyzer

an = gsanalyzer.GsAnalyzer("reportp9.txt")

an.compareAllPaths("report_path.txt")
an.compareAllKeys("report_keys.txt")

