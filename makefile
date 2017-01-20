main.pdf: main.ps laser635.tex
	ps2pdf main.ps

main.dvi: main.tex laser635.tex
	latex main.tex

main.ps: main.dvi
	dvips -Ppdf -G0 main.dvi

clean:
	rm *.log
	rm *.dvi
 
