test.pdf: test.ps test.tex
	ps2pdf test.ps

test.dvi: test.tex
	latex test.tex

test.ps: test.dvi
	dvips -Ppdf -G0 test.dvi

clean:
	rm *.log
	rm *.dvi