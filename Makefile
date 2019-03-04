NO := 1
FILE := lab$(NO)

all: clean-latex compile clean-scripts open-pdf post-latex
latex: clean-latex compile open-pdf post-latex
clean-latex:
	-rm -fr $(FILE).bbl
	-rm -fr $(FILE).bcf
	-rm -fr $(FILE).blg
	-rm -fr $(FILE).aux
	-rm -fr $(FILE).out
	-rm -fr $(FILE).run.xml
	-rm -fr $(FILE).log
	-rm -fr texput.log

post-latex:
	$(MAKE) clean-latex

clean-scripts:

compile:
	pdflatex $(FILE)
	-biber --output-safechars $(FILE)
	-pdflatex $(FILE)

open-pdf:
	open $(FILE).pdf