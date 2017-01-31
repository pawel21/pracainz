main.pdf: main.ps laser635.tex laser850vcsel.tex laser850edge.tex teoria.tex laser980.tex laserCommon.tex pomiar.tex bibliografia.tex wstep.tex komunikacja.tex program_do_sterowania.tex
	ps2pdf main.ps

main.dvi: main.tex laser635.tex laser850vcsel.tex laser850edge.tex laser980.tex teoria.tex laserCommon.tex  pomiar.tex bibliografia.tex wstep.tex komunikacja.tex program_do_sterowania.tex
	latex main.tex

main.ps: main.dvi
	dvips -Ppdf -G0 main.dvi

clean:
	rm *.log
	rm *.dvi
 
